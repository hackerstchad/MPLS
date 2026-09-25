#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 MPLS Protocol Advanced Simulator & 3D Visualizer
 Title: MPLS (Hackers_tchad)
 Version: 3.0.0
 Author: Hackers_tchad Research Lab
 Description:
     A production-grade educational toolkit that deeply simulates MPLS (Multi-
     Protocol Label Switching). It covers LDP, RSVP-TE, BGP-LU, Segment Routing
     MPLS, LFIB building, TTL/EXP handling, PHP, UHP, L3VPN/L2VPN integration,
     Fast Reroute (FRR), OAM/ BFD echoes, and a stylized pseudo-3D canvas.
================================================================================
"""

import os
import sys
import time
import math
import random
import logging
import argparse
import threading
import queue
import json
import copy
import re
import collections
import itertools
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Optional, Set, Callable, Any, Union
from enum import Enum, auto
from collections import defaultdict, deque

# ---------------------------------------------------------------------------
# Optional external dependencies
# ---------------------------------------------------------------------------
try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    np = None
    logging.warning("numpy not installed: matrix helpers disabled")

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception as exc:  # pragma: no cover
    Image = ImageDraw = ImageFont = None
    logging.warning("PIL not installed: export features disabled")

try:
    import yaml
except Exception as exc:  # pragma: no cover
    yaml = None
    logging.warning("pyyaml not installed: YAML import disabled")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger("MPLS_Hackers_tchad")


# ############################################################################
# SECTION 1: ENUMERATIONS & CONSTANTS
# ############################################################################

class LabelAction(Enum):
    """Possible LFIB (Label Forwarding Information Base) actions."""
    PUSH = auto()
    POP = auto()
    SWAP = auto()
    NOOP = auto()
    DROP = auto()
    FORWARD = auto()


class DistributionMode(Enum):
    """Label distribution modes."""
    DU = "unsolicited_downstream"
    DOD = "downstream_on_demand"
    Ordered = "ordered_control"
    Independent = "independent_control"


class TunnelStyle(Enum):
    """RSVP-TE tunnel computation styles."""
    SHORTEST_IGP = auto()
    CSPF = auto()
    EXPLICIT_ROUTE = auto()
    SRLG_DISJOINT = auto()


class ProtectionType(Enum):
    """Fast Reroute protection flavors."""
    LINK_PROTECTION = auto()
    NODE_PROTECTION = auto()
    FACILITY_BACKUP = auto()
    ONE_TO_ONE_BACKUP = auto()
    NONE = auto()


class MessageType(Enum):
    """Internal event bus message types."""
    HELLO = auto()
    LDP_HELLO = auto()
    LDP_MAPPING = auto()
    LDP_REQUEST = auto()
    LDP_RELEASE = auto()
    LDP_WITHDRAW = auto()
    RSVP_PATH = auto()
    RSVP_RESV = auto()
    RSVP_PATHERR = auto()
    RSVP_RESVERR = auto()
    BGP_UPDATE = auto()
    BFD_HELLO = auto()
    OAM_PING = auto()
    OAM_TRACEROUTE = auto()
    FRR_SWITCH = auto()
    FRR_REVERT = auto()


class VPNType(Enum):
    """VPN family types."""
    L3VPN = auto()
    L2VPN_VPWS = auto()
    L2VPN_VPLS = auto()
    EVPN = auto()


class FECType(Enum):
    """Types of Forwarding Equivalence Class."""
    IGP_PREFIX = auto()
    BGP_VPNV4 = auto()
    BGP_VPNV6 = auto()
    LDP_PEER = auto()
    RSVP_TUNNEL = auto()
    SR_PREFIX_SID = auto()
    SR_ADJ_SID = auto()
    L2VPN_PW = auto()


class AddressFamily(Enum):
    """Address families used by MPLS control-plane protocols."""
    IPV4 = 1
    IPV6 = 2


# Well-known MPLS label values (RFC 3032 / RFC 7274)
SPECIAL_LABELS = {
    0: "IPv4 Explicit NULL",
    1: "Router Alert",
    2: "IPv6 Explicit NULL",
    3: "Implicit NULL",
    4: "OAM Alert (G-ACh)",
    7: "Entropy Label Indicator",
    13: "GAL (Generic Associated Channel Label)",
    14: "Router Alert (OAM)",
}

DEFAULT_LABEL_MIN = 16
DEFAULT_LABEL_MAX = 1048575
DEFAULT_TTL = 64

# Stylized palette for the 3D Tkinter canvas
THEME = {
    "bg": "#050510",
    "grid": "#1a1a2e",
    "node": "#00f0ff",
    "node_border": "#ffffff",
    "edge": "#444466",
    "edge_active": "#ff00aa",
    "label_stack": "#ffe600",
    "text": "#00ffcc",
    "panel": "#0a0a18",
    "accent": "#ff0055",
    "success": "#00ff66",
    "warning": "#ffaa00",
}


# ############################################################################
# SECTION 2: DATA CLASSES
# ############################################################################

@dataclass
class MPLSLabel:
    """Single MPLS label entry with label value, TC/EXP, S-bit, TTL."""
    value: int
    tc: int = 0
    s: int = 1
    ttl: int = DEFAULT_TTL

    def encode(self) -> int:
        """Encode to a 32-bit MPLS shim header."""
        if not (0 <= self.value <= DEFAULT_LABEL_MAX):
            raise ValueError("Label value out of range")
        if not (0 <= self.tc <= 7):
            raise ValueError("TC/EXP out of range")
        if not (0 <= self.s <= 1):
            raise ValueError("S-bit out of range")
        if not (0 <= self.ttl <= 255):
            raise ValueError("TTL out of range")
        return (self.value << 12) | (self.tc << 9) | (self.s << 8) | self.ttl

    @classmethod
    def decode(cls, word: int) -> "MPLSLabel":
        value = (word >> 12) & DEFAULT_LABEL_MAX
        tc = (word >> 9) & 0x7
        s = (word >> 8) & 0x1
        ttl = word & 0xFF
        return cls(value, tc, s, ttl)

    def copy(self, ttl_decrement: int = 0) -> "MPLSLabel":
        return MPLSLabel(
            value=self.value,
            tc=self.tc,
            s=self.s,
            ttl=max(0, self.ttl - ttl_decrement),
        )

    def __repr__(self) -> str:
        name = SPECIAL_LABELS.get(self.value, str(self.value))
        return f"MPLSLabel({name}, TC={self.tc}, S={self.s}, TTL={self.ttl})"


@dataclass
class FEC:
    """Forwarding Equivalence Class descriptor."""
    prefix: str
    prefix_len: int = 32
    fec_type: FECType = FECType.IGP_PREFIX
    rd: Optional[str] = None
    vpn: Optional[str] = None
    color: Optional[int] = None
    tunnel_id: Optional[str] = None
    sid: Optional[int] = None
    affinity: int = 0

    def key(self) -> str:
        return f"{self.rd or ''}:{self.prefix}/{self.prefix_len}:{self.fec_type.name}"

    def __hash__(self) -> int:
        return hash(self.key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, FEC) and self.key() == other.key()


@dataclass
class LFIBEntry:
    """One row in the Label Forwarding Information Base."""
    in_label: int
    fec: FEC
    action: LabelAction
    out_label: Optional[int] = None
    next_hop: Optional[str] = None
    outgoing_intf: Optional[str] = None
    operation_detail: str = ""
    backup_next_hop: Optional[str] = None
    backup_out_intf: Optional[str] = None
    is_bkup_active: bool = False
    tunnel_ref: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "in_label": self.in_label,
            "fec": self.fec.key(),
            "action": self.action.name,
            "out_label": self.out_label,
            "next_hop": self.next_hop,
            "outgoing_intf": self.outgoing_intf,
            "operation_detail": self.operation_detail,
            "backup_next_hop": self.backup_next_hop,
            "backup_out_intf": self.backup_out_intf,
            "is_bkup_active": self.is_bkup_active,
            "tunnel_ref": self.tunnel_ref,
        }


@dataclass
class Interface:
    """Router interface with MPLS capability flags."""
    name: str
    ip: Optional[str] = None
    state: str = "up"
    mtu: int = 1500
    bandwidth: int = 1000000
    reservable_bandwidth: int = 1000000
    admin_group: int = 0
    srlg: List[int] = field(default_factory=list)
    mpls_enabled: bool = True
    ldp_enabled: bool = True
    rsvp_enabled: bool = False
    sr_enabled: bool = False
    metric: int = 10


@dataclass
class Link:
    """Unidirectional link between two routers."""
    source: str
    target: str
    source_intf: str
    target_intf: str
    metric: int = 10
    bandwidth: int = 1000000
    delay_ms: float = 1.0
    admin_group: int = 0
    srlg: List[int] = field(default_factory=list)
    protection: ProtectionType = ProtectionType.NONE


@dataclass
class Packet:
    """MPLS packet traversing the simulated network."""
    packet_id: str
    labels: List[MPLSLabel] = field(default_factory=list)
    payload: bytes = b""
    src: Optional[str] = None
    dst: Optional[str] = None
    path: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=time.time)
    history: List[Dict[str, Any]] = field(default_factory=list)
    color: str = "#00ffcc"
    vpn_type: Optional[VPNType] = None
    fec: Optional[FEC] = None

    def top_label(self) -> Optional[MPLSLabel]:
        return self.labels[-1] if self.labels else None

    def push(self, label: MPLSLabel) -> None:
        if self.labels:
            self.labels[-1].s = 0
        self.labels.append(label)

    def pop(self) -> Optional[MPLSLabel]:
        if not self.labels:
            return None
        top = self.labels.pop()
        if self.labels:
            self.labels[-1].s = 1
        return top

    def swap(self, new_value: int) -> None:
        if self.labels:
            self.labels[-1].value = new_value

    def copy(self) -> "Packet":
        return Packet(
            packet_id=self.packet_id,
            labels=[lbl.copy() for lbl in self.labels],
            payload=self.payload,
            src=self.src,
            dst=self.dst,
            path=self.path.copy(),
            timestamp=self.timestamp,
            history=[h.copy() for h in self.history],
            color=self.color,
            vpn_type=self.vpn_type,
            fec=copy.deepcopy(self.fec),
        )


@dataclass
class Message:
    """Internal control-plane message exchanged between routers."""
    msg_type: MessageType
    src_router: str
    dst_router: str
    payload: Dict[str, Any] = field(default_factory=dict)
    ttl: int = 64


@dataclass
class Tunnel:
    """RSVP-TE or SR tunnel abstraction."""
    name: str
    headend: str
    tailend: str
    path: List[str] = field(default_factory=list)
    style: TunnelStyle = TunnelStyle.SHORTEST_IGP
    bandwidth: int = 0
    affinity: int = 0
    exclude_admin_groups: Set[int] = field(default_factory=set)
    protection: ProtectionType = ProtectionType.NONE
    tunnel_label_stack: List[int] = field(default_factory=list)
    backup_path: Optional[List[str]] = None
    is_active: bool = False
    is_frr_active: bool = False


@dataclass
class VPNRoute:
    """VPNv4/VPNv6 route with RD and RT."""
    rd: str
    prefix: str
    prefix_len: int
    rt_import: List[str] = field(default_factory=list)
    rt_export: List[str] = field(default_factory=list)
    next_hop: Optional[str] = None
    inner_label: Optional[int] = None
    vpn_type: VPNType = VPNType.L3VPN


# ############################################################################
# SECTION 3: UTILITY FUNCTIONS
# ############################################################################

def ip_to_int(addr: str) -> int:
    """Convert dotted IPv4 to integer."""
    parts = [int(p) for p in addr.split(".")]
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]


def int_to_ip(value: int) -> str:
    """Convert integer to dotted IPv4."""
    return f"{(value >> 24) & 0xFF}.{(value >> 16) & 0xFF}.{(value >> 8) & 0xFF}.{value & 0xFF}"


def prefix_match(prefix: str, prefix_len: int, addr: str) -> bool:
    """Check if address belongs to prefix/len."""
    try:
        net = ip_to_int(prefix) & (0xFFFFFFFF << (32 - prefix_len))
        host = ip_to_int(addr)
        return (host & (0xFFFFFFFF << (32 - prefix_len))) == net
    except Exception:
        return False


def generate_router_id(name: str) -> str:
    """Generate a deterministic router-id from a name hash."""
    h = hash(name) & 0xFFFFFFFF
    return int_to_ip(h)


def random_label_pool(size: int = 5000) -> List[int]:
    """Create a randomized label pool."""
    pool = list(range(DEFAULT_LABEL_MIN, DEFAULT_LABEL_MIN + size))
    random.shuffle(pool)
    return pool


def path_cost(path: List[str], links: List[Link], metric_attr: str = "metric") -> float:
    """Compute total metric of a path over link list."""
    total = 0.0
    for i in range(len(path) - 1):
        found = [l for l in links if l.source == path[i] and l.target == path[i + 1]]
        total += float(getattr(found[0], metric_attr)) if found else 1e9
    return total


def longest_prefix_match(prefixes: List[Tuple[str, int]], addr: str) -> Optional[Tuple[str, int]]:
    """Return longest matching prefix."""
    best: Optional[Tuple[str, int]] = None
    best_len = -1
    for p, plen in prefixes:
        if prefix_match(p, plen, addr) and plen > best_len:
            best = (p, plen)
            best_len = plen
    return best


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def hsl_to_hex(h: float, s: float, l: float) -> str:
    """Convert HSL to hex color."""
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    return f"#{int((r + m) * 255):02x}{int((g + m) * 255):02x}{int((b + m) * 255):02x}"


def packet_id_gen() -> str:
    return f"P{int(time.time() * 1000000) % 100000000:08d}"


def indent_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, default=str)


# ############################################################################
# SECTION 4: CONTROL PLANE: LDP, RSVP-TE, BGP-LU, SEGMENT ROUTING
# ############################################################################

class LabelManager:
    """Per-router label allocation and accounting."""

    def __init__(self, router_name: str, pool_size: int = 5000):
        self.router_name = router_name
        self.pool = random_label_pool(pool_size)
        self.allocated: Dict[int, Any] = {}
        self.remote_bindings: Dict[str, Dict[FEC, int]] = defaultdict(dict)

    def allocate(self, context: Any) -> int:
        while self.pool:
            lbl = self.pool.pop()
            if lbl not in self.allocated:
                self.allocated[lbl] = context
                return lbl
        raise RuntimeError(f"[{self.router_name}] Label pool exhausted")

    def release(self, label: int) -> None:
        if label in self.allocated:
            del self.allocated[label]
            self.pool.append(label)

    def get_remote(self, neighbor: str, fec: FEC) -> Optional[int]:
        return self.remote_bindings.get(neighbor, {}).get(fec)

    def set_remote(self, neighbor: str, fec: FEC, label: int) -> None:
        self.remote_bindings[neighbor][fec] = label


class ForwardingPlane:
    """LFIB and MPLS forwarding engine for one router."""

    def __init__(self, router_name: str, mgr: LabelManager):
        self.router_name = router_name
        self.mgr = mgr
        self.lfib: Dict[int, LFIBEntry] = {}
        self.fec_to_local_label: Dict[FEC, int] = {}
        self.ip_routes: Dict[FEC, Tuple[str, str]] = {}  # fec -> (next_hop, intf)
        self.statistics = defaultdict(int)

    def install_lfib_entry(self, entry: LFIBEntry) -> None:
        self.lfib[entry.in_label] = entry
        self.fec_to_local_label[entry.fec] = entry.in_label
        logger.debug(f"[{self.router_name}] install LFIB in={entry.in_label} {entry.action.name}")

    def remove_lfib_entry(self, in_label: int) -> None:
        entry = self.lfib.pop(in_label, None)
        if entry and entry.fec in self.fec_to_local_label:
            del self.fec_to_local_label[entry.fec]

    def lookup(self, label: int) -> Optional[LFIBEntry]:
        self.statistics["lookup"] += 1
        return self.lfib.get(label)

    def resolve_fec(self, fec: FEC) -> Optional[Tuple[str, str]]:
        return self.ip_routes.get(fec)

    def process_packet(self, pkt: Packet, in_intf: Optional[str] = None) -> Optional[Tuple[str, str, Packet]]:
        """Process one MPLS packet. Returns (out_intf, next_hop, modified_packet) or None."""
        top = pkt.top_label()
        if not top:
            self.statistics["native_ip"] += 1
            return None
        if top.ttl <= 1:
            self.statistics["ttl_exceeded"] += 1
            pkt.history.append({"node": self.router_name, "event": "TTL_EXPIRED"})
            return None

        entry = self.lookup(top.value)
        if not entry:
            self.statistics["unlabeled_drop"] += 1
            pkt.history.append({"node": self.router_name, "event": "LABEL_UNKNOWN", "label": top.value})
            return None

        pkt.history.append({
            "node": self.router_name,
            "in_label": top.value,
            "action": entry.action.name,
            "fec": entry.fec.key(),
        })

        nh = entry.backup_next_hop if entry.is_bkup_active and entry.backup_next_hop else entry.next_hop
        oif = entry.backup_out_intf if entry.is_bkup_active and entry.backup_out_intf else entry.outgoing_intf

        if entry.action == LabelAction.POP:
            popped = pkt.pop()
            if popped:
                popped.ttl -= 1
            self.statistics["pop"] += 1
        elif entry.action == LabelAction.SWAP:
            pkt.swap(entry.out_label if entry.out_label is not None else top.value)
            top.ttl -= 1
            self.statistics["swap"] += 1
        elif entry.action == LabelAction.PUSH:
            pkt.push(MPLSLabel(value=entry.out_label or top.value, s=1, ttl=top.ttl - 1))
            top.s = 0
            self.statistics["push"] += 1
        elif entry.action == LabelAction.FORWARD:
            top.ttl -= 1
            self.statistics["forward"] += 1
        elif entry.action == LabelAction.DROP:
            self.statistics["drop"] += 1
            return None
        else:
            top.ttl -= 1

        return oif, nh, pkt


class MPLSRouter:
    """Full-featured MPLS-capable router."""

    def __init__(self, name: str, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.name = name
        self.router_id = generate_router_id(name)
        self.interfaces: Dict[str, Interface] = {}
        self.neighbors: Dict[str, Dict[str, Any]] = {}
        self.label_mgr = LabelManager(name)
        self.fwd = ForwardingPlane(name, self.label_mgr)
        self.ldp_enabled = True
        self.rsvp_enabled = False
        self.sr_enabled = False
        self.bgp_enabled = False
        self.ldp_session_state: Dict[str, str] = {}
        self.tunnels: Dict[str, Tunnel] = {}
        self.vpn_routes: List[VPNRoute] = []
        self.position = (x, y, z)
        self.is_pes = False
        self.is_p = False
        self.is_ce = False
        self.sr_prefix_sid: Optional[int] = None
        self.sr_adj_sids: Dict[str, int] = {}
        self.bfd_sessions: Dict[str, Dict[str, Any]] = {}
        self.oam_stats = {"ping": 0, "traceroute": 0}

    def add_interface(self, intf: Interface) -> None:
        self.interfaces[intf.name] = intf

    def get_interface(self, name: str) -> Optional[Interface]:
        return self.interfaces.get(name)

    def allocate_local_label(self, fec: FEC) -> int:
        if fec in self.fwd.fec_to_local_label:
            return self.fwd.fec_to_local_label[fec]
        lbl = self.label_mgr.allocate(fec)
        return lbl

    def ldp_hello_to(self, neighbor: str) -> Message:
        return Message(
            msg_type=MessageType.LDP_HELLO,
            src_router=self.name,
            dst_router=neighbor,
            payload={"router_id": self.router_id, "transport_addr": self.router_id},
        )

    def ldp_mapping_for(self, fec: FEC, neighbor: str) -> Message:
        local_label = self.allocate_local_label(fec)
        return Message(
            msg_type=MessageType.LDP_MAPPING,
            src_router=self.name,
            dst_router=neighbor,
            payload={"fec": asdict(fec), "label": local_label, "mode": DistributionMode.DU.value},
        )

    def build_lfib_from_ldp(self, network: "MPLSNetwork") -> None:
        """Build LFIB rows using LDP DU bindings."""
        for fec, local_label in list(self.fwd.fec_to_local_label.items()):
            # resolve next-hop via IGP (simple: neighbor that advertises FEC reachability)
            nh_name = self._resolve_next_hop(network, fec)
            if not nh_name:
                continue
            remote_label = self.label_mgr.get_remote(nh_name, fec)
            out_intf = self._intf_to_neighbor(nh_name)
            if remote_label is None:
                # PHP: implicit null means pop before sending
                entry = LFIBEntry(
                    in_label=local_label,
                    fec=fec,
                    action=LabelAction.POP,
                    next_hop=nh_name,
                    outgoing_intf=out_intf,
                    operation_detail="PHP: downstream advertised implicit-null",
                )
            else:
                entry = LFIBEntry(
                    in_label=local_label,
                    fec=fec,
                    action=LabelAction.SWAP,
                    out_label=remote_label,
                    next_hop=nh_name,
                    outgoing_intf=out_intf,
                    operation_detail=f"swap to {remote_label} toward {nh_name}",
                )
            self.fwd.install_lfib_entry(entry)

    def _resolve_next_hop(self, network: "MPLSNetwork", fec: FEC) -> Optional[str]:
        """Simple next-hop resolution: choose neighbor closest to destination."""
        dest = fec.prefix
        candidates = []
        for nbr in self.neighbors:
            # If neighbor router-id matches destination prefix /32
            if prefix_match(dest, fec.prefix_len, network.routers[nbr].router_id):
                candidates.append(nbr)
        if not candidates:
            # fallback: any neighbor
            candidates = list(self.neighbors.keys())
        return candidates[0] if candidates else None

    def _intf_to_neighbor(self, neighbor: str) -> Optional[str]:
        for name, info in self.neighbors.items():
            if name == neighbor:
                return info.get("local_intf")
        return None

    def build_sr_lfib(self, network: "MPLSNetwork") -> None:
        """Build LFIB entries for Segment Routing MPLS prefix-SIDs and adj-SIDs."""
        if not self.sr_enabled:
            return
        # Adjacency SID per outgoing interface
        for nbr_name, info in self.neighbors.items():
            adj_sid = self.label_mgr.allocate(f"adj-{nbr_name}")
            self.sr_adj_sids[nbr_name] = adj_sid
            entry = LFIBEntry(
                in_label=adj_sid,
                fec=FEC(prefix=network.routers[nbr_name].router_id, fec_type=FECType.SR_ADJ_SID),
                action=LabelAction.FORWARD,
                next_hop=nbr_name,
                outgoing_intf=info.get("local_intf"),
                operation_detail=f"SR Adj-SID pop-and-forward to {nbr_name}",
            )
            self.fwd.install_lfib_entry(entry)

        # Prefix SID for local node
        if self.sr_prefix_sid:
            local_sid_fec = FEC(prefix=self.router_id, fec_type=FECType.SR_PREFIX_SID, sid=self.sr_prefix_sid)
            local_label = self.allocate_local_label(local_sid_fec)
            nh = self._resolve_next_hop(network, local_sid_fec)
            out_intf = self._intf_to_neighbor(nh) if nh else None
            # If we are the origin, just pop and continue IP lookup
            entry = LFIBEntry(
                in_label=local_label,
                fec=local_sid_fec,
                action=LabelAction.POP,
                next_hop=nh,
                outgoing_intf=out_intf,
                operation_detail="Local SR Prefix-SID: pop",
            )
            self.fwd.install_lfib_entry(entry)

    def build_rsvp_tunnel(self, network: "MPLSNetwork", tunnel: Tunnel) -> None:
        """Compute ERO and install LFIB tunnel entries."""
        path = network.shortest_path(tunnel.headend, tunnel.tailend)
        tunnel.path = path
        tunnel.is_active = True
        self.tunnels[tunnel.name] = tunnel
        # Install per-hop labels: headend pushes full stack, midpoints swap.
        labels = []
        for idx, node in enumerate(path[:-1]):
            lbl = network.routers[node].label_mgr.allocate(f"TE-{tunnel.name}-{idx}")
            labels.append(lbl)
        tunnel.tunnel_label_stack = labels
        # Headend entry not in LFIB, but application pushes stack.
        for i in range(1, len(path) - 1):
            node = path[i]
            router = network.routers[node]
            in_lbl = labels[i - 1]
            out_lbl = labels[i]
            nh = path[i + 1]
            out_intf = router._intf_to_neighbor(nh)
            entry = LFIBEntry(
                in_label=in_lbl,
                fec=FEC(prefix=tunnel.tailend, tunnel_id=tunnel.name, fec_type=FECType.RSVP_TUNNEL),
                action=LabelAction.SWAP,
                out_label=out_lbl,
                next_hop=nh,
                outgoing_intf=out_intf,
                tunnel_ref=tunnel.name,
                operation_detail=f"RSVP-TE {tunnel.name} swap {in_lbl}->{out_lbl}",
            )
            router.fwd.install_lfib_entry(entry)
        # Tailend pop
        tail = network.routers[path[-1]]
        tail_entry = LFIBEntry(
            in_label=labels[-1],
            fec=FEC(prefix=tunnel.tailend, tunnel_id=tunnel.name, fec_type=FECType.RSVP_TUNNEL),
            action=LabelAction.POP,
            operation_detail=f"RSVP-TE {tunnel.name} tailend pop",
        )
        tail.fwd.install_lfib_entry(tail_entry)

    def enable_bfd(self, neighbor: str, interval_ms: int = 300) -> None:
        self.bfd_sessions[neighbor] = {
            "state": "up",
            "interval_ms": interval_ms,
            "last_rx": time.time(),
            "missed": 0,
        }

    def receive_control_message(self, msg: Message, network: "MPLSNetwork") -> List[Message]:
        """Handle LDP/RSVP/BGP/OAM messages."""
        replies: List[Message] = []
        if msg.msg_type == MessageType.LDP_HELLO:
            self.ldp_session_state[msg.src_router] = "operational"
            replies.append(Message(MessageType.LDP_HELLO, self.name, msg.src_router))
        elif msg.msg_type == MessageType.LDP_MAPPING:
            fec_data = msg.payload.get("fec", {})
            fec = FEC(
                prefix=fec_data.get("prefix", ""),
                prefix_len=fec_data.get("prefix_len", 32),
                fec_type=FECType[fec_data.get("fec_type", "IGP_PREFIX")],
            )
            self.label_mgr.set_remote(msg.src_router, fec, msg.payload["label"])
        elif msg.msg_type == MessageType.RSVP_PATH:
            tunnel_name = msg.payload.get("tunnel_name")
            if tunnel_name in self.tunnels:
                replies.append(Message(MessageType.RSVP_RESV, self.name, msg.src_router, {"tunnel_name": tunnel_name}))
        elif msg.msg_type == MessageType.BGP_UPDATE:
            vpn_route = VPNRoute(
                rd=msg.payload.get("rd"),
                prefix=msg.payload.get("prefix"),
                prefix_len=msg.payload.get("prefix_len", 32),
                rt_import=msg.payload.get("rt_import", []),
                rt_export=msg.payload.get("rt_export", []),
                next_hop=msg.payload.get("next_hop"),
                inner_label=msg.payload.get("inner_label"),
                vpn_type=VPNType[msg.payload.get("vpn_type", "L3VPN")],
            )
            self.vpn_routes.append(vpn_route)
        elif msg.msg_type == MessageType.BFD_HELLO:
            self.bfd_sessions.setdefault(msg.src_router, {"state": "up", "last_rx": time.time()})
            self.bfd_sessions[msg.src_router]["last_rx"] = time.time()
            self.bfd_sessions[msg.src_router]["missed"] = 0
        elif msg.msg_type == MessageType.OAM_PING:
            self.oam_stats["ping"] += 1
            replies.append(Message(MessageType.OAM_PING, self.name, msg.src_router, {"reply": True, "node": self.name}))
        elif msg.msg_type == MessageType.OAM_TRACEROUTE:
            self.oam_stats["traceroute"] += 1
            replies.append(Message(MessageType.OAM_TRACEROUTE, self.name, msg.src_router, {"hop": self.name}))
        return replies

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "router_id": self.router_id,
            "position": self.position,
            "interfaces": {k: asdict(v) for k, v in self.interfaces.items()},
            "ldp_sessions": self.ldp_session_state,
            "tunnels": {k: asdict(v) for k, v in self.tunnels.items()},
            "lfib": [e.to_dict() for e in self.fwd.lfib.values()],
            "statistics": dict(self.fwd.statistics),
        }


# ############################################################################
# SECTION 5: NETWORK TOPOLOGY & PATH COMPUTATION
# ############################################################################

class MPLSNetwork:
    """Container for routers, links, and global computations."""

    def __init__(self):
        self.routers: Dict[str, MPLSRouter] = {}
        self.links: List[Link] = []
        self.topology_version = 0
        self.event_log: List[str] = []
        self._lock = threading.RLock()

    def add_router(self, router: MPLSRouter) -> None:
        with self._lock:
            self.routers[router.name] = router

    def add_link(self, link: Link) -> None:
        with self._lock:
            self.links.append(link)
            self._update_neighbors(link)
            self.topology_version += 1

    def _update_neighbors(self, link: Link) -> None:
        src = self.routers.get(link.source)
        dst = self.routers.get(link.target)
        if src:
            src.neighbors[link.target] = {"local_intf": link.source_intf, "remote_intf": link.target_intf}
        if dst:
            dst.neighbors[link.source] = {"local_intf": link.target_intf, "remote_intf": link.source_intf}

    def get_link(self, a: str, b: str) -> Optional[Link]:
        for l in self.links:
            if l.source == a and l.target == b:
                return l
        return None

    def shortest_path(self, src: str, dst: str, weight: str = "metric") -> List[str]:
        """Dijkstra shortest path on directed links."""
        if src not in self.routers or dst not in self.routers:
            return []
        dist: Dict[str, float] = {r: float("inf") for r in self.routers}
        prev: Dict[str, Optional[str]] = {r: None for r in self.routers}
        dist[src] = 0.0
        visited: Set[str] = set()
        while True:
            unvisited = {r: d for r, d in dist.items() if r not in visited}
            if not unvisited:
                break
            u = min(unvisited, key=unvisited.get)
            visited.add(u)
            if u == dst:
                break
            for l in self.links:
                if l.source == u and l.target in self.routers:
                    w = float(getattr(l, weight, 1))
                    if dist[u] + w < dist[l.target]:
                        dist[l.target] = dist[u] + w
                        prev[l.target] = u
        path: List[str] = []
        cur: Optional[str] = dst
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        return list(reversed(path))

    def cspf_path(self, src: str, dst: str, bandwidth: int = 0,
                  affinity: int = 0, exclude: Set[int] = set()) -> List[str]:
        """Constrained SPF filtering links by bandwidth/admin-groups."""
        valid_links = [
            l for l in self.links
            if l.bandwidth >= bandwidth and not (l.admin_group & affinity) and not (l.admin_group in exclude)
        ]
        # Use a temporary network view for Dijkstra
        temp = MPLSNetwork()
        temp.routers = self.routers
        temp.links = valid_links
        return temp.shortest_path(src, dst)

    def k_shortest_paths(self, src: str, dst: str, k: int = 3) -> List[List[str]]:
        """Yen's k-shortest loopless paths."""
        shortest = self.shortest_path(src, dst)
        if not shortest:
            return []
        candidates: List[Tuple[float, List[str]]] = []
        result: List[List[str]] = [shortest]
        for _ in range(k - 1):
            for i in range(len(result[-1]) - 1):
                spur_node = result[-1][i]
                root_path = result[-1][:i + 1]
                removed_links: List[Link] = []
                for p in result:
                    if len(p) > i and p[:i + 1] == root_path:
                        l = self.get_link(p[i], p[i + 1])
                        if l and l in self.links:
                            removed_links.append(l)
                            self.links.remove(l)
                spur_path = self.shortest_path(spur_node, dst)
                for l in removed_links:
                    self.links.append(l)
                if spur_path:
                    total = root_path[:-1] + spur_path
                    cost = path_cost(total, self.links)
                    if total not in [r for _, r in candidates] and total not in result:
                        candidates.append((cost, total))
            if not candidates:
                break
            candidates.sort(key=lambda x: x[0])
            result.append(candidates.pop(0)[1])
        return result

    def sr_path_to_sid_list(self, path: List[str]) -> List[int]:
        """Convert a node path to SR prefix-SID list."""
        sids = []
        for node in path[1:]:
            r = self.routers.get(node)
            if r and r.sr_prefix_sid:
                sids.append(r.sr_prefix_sid)
        return sids

    def build_all_ldp(self) -> None:
        """Exchange LDP hellos/mappings and build LFIBs."""
        messages: List[Message] = []
        for r in self.routers.values():
            for nbr in r.neighbors:
                messages.append(r.ldp_hello_to(nbr))
        # Process hellos (state transitions)
        for msg in messages:
            self.routers[msg.dst_router].receive_control_message(msg, self)
        # Generate mapping advertisements for every router FEC (loopback)
        mappings: List[Message] = []
        for r in self.routers.values():
            fec = FEC(prefix=r.router_id, prefix_len=32, fec_type=FECType.IGP_PREFIX)
            r.allocate_local_label(fec)
            for nbr in r.neighbors:
                mappings.append(r.ldp_mapping_for(fec, nbr))
        for msg in mappings:
            self.routers[msg.dst_router].receive_control_message(msg, self)
        # Build LFIBs
        for r in self.routers.values():
            r.build_lfib_from_ldp(self)

    def build_all_sr(self) -> None:
        for r in self.routers.values():
            if r.sr_enabled:
                r.build_sr_lfib(self)

    def build_all_tunnels(self) -> None:
        for r in self.routers.values():
            for t in list(r.tunnels.values()):
                r.build_rsvp_tunnel(self, t)

    def propagate_packet(self, pkt: Packet, start_router: str,
                         callback: Optional[Callable[[str, Packet], None]] = None) -> Packet:
        """Walk packet through LFIB from start router until drop/delivery."""
        current = start_router
        max_hops = 100
        hops = 0
        while current and hops < max_hops:
            router = self.routers.get(current)
            if not router:
                break
            pkt.path.append(current)
            result = router.fwd.process_packet(pkt)
            if callback:
                callback(current, pkt)
            if result is None:
                break
            oif, nh, pkt = result
            if not nh:
                break
            current = nh
            hops += 1
        return pkt

    def ping(self, src: str, dst: str, count: int = 5,
             callback: Optional[Callable[[str, Packet], None]] = None) -> Dict[str, Any]:
        """MPLS LSP ping using implicit-null / explicit-null."""
        results = []
        fec = FEC(prefix=self.routers[dst].router_id, prefix_len=32, fec_type=FECType.IGP_PREFIX)
        local_lbl = self.routers[src].fwd.fec_to_local_label.get(fec)
        for _ in range(count):
            pkt = Packet(packet_id=packet_id_gen(), src=src, dst=dst)
            if local_lbl is not None:
                pkt.push(MPLSLabel(value=local_lbl))
            pkt = self.propagate_packet(pkt, src, callback)
            success = bool(pkt.labels) and pkt.path[-1] == dst
            results.append({"success": success, "path": pkt.path.copy(), "history": pkt.history.copy()})
        return {"src": src, "dst": dst, "count": count, "results": results}

    def traceroute(self, src: str, dst: str) -> Dict[str, Any]:
        """MPLS traceroute revealing LFIB actions per hop."""
        fec = FEC(prefix=self.routers[dst].router_id, prefix_len=32, fec_type=FECType.IGP_PREFIX)
        local_lbl = self.routers[src].fwd.fec_to_local_label.get(fec)
        pkt = Packet(packet_id=packet_id_gen(), src=src, dst=dst)
        if local_lbl is not None:
            pkt.push(MPLSLabel(value=local_lbl))
        pkt = self.propagate_packet(pkt, src)
        hops = []
        for h in pkt.history:
            hops.append({
                "node": h.get("node"),
                "action": h.get("action"),
                "label": h.get("in_label"),
            })
        return {"src": src, "dst": dst, "hops": hops}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "routers": {k: v.to_dict() for k, v in self.routers.items()},
            "links": [asdict(l) for l in self.links],
            "topology_version": self.topology_version,
        }


# ############################################################################
# SECTION 6: TKINTER 3D VISUALIZER
# ############################################################################

class MPLSVisualizer3D:
    """Stylized pseudo-3D Tkinter canvas for MPLS network."""

    def __init__(self, network: MPLSNetwork, width: int = 1400, height: int = 900):
        self.network = network
        self.width = width
        self.height = height
        self.root = None
        self.canvas = None
        self.running = False
        self.scale = 60.0
        self.rot_x = 0.45
        self.rot_y = 0.55
        self.pan_x = width / 2
        self.pan_y = height / 2
        self.anim_packets: List[Dict[str, Any]] = []
        self.node_circles: Dict[str, int] = {}
        self.edge_lines: Dict[Tuple[str, str], int] = {}
        self._drag_start: Optional[Tuple[int, int]] = None

    def project(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        """Apply rotation and perspective projection."""
        cx, sx = math.cos(self.rot_x), math.sin(self.rot_x)
        cy, sy = math.cos(self.rot_y), math.sin(self.rot_y)
        # rotate around X then Y
        y1 = y * cx - z * sx
        z1 = y * sx + z * cx
        x1 = x * cy + z1 * sy
        z2 = -x * sy + z1 * cy
        # perspective
        fov = 800
        if z2 + fov <= 0:
            z2 = -fov + 1
        factor = fov / (fov + z2)
        px = x1 * self.scale * factor + self.pan_x
        py = y1 * self.scale * factor + self.pan_y
        return px, py, z2

    def build_ui(self) -> None:
        import tkinter as tk
        from tkinter import ttk
        self.root = tk.Tk()
        self.root.title("MPLS (Hackers_tchad) - Advanced 3D Visualizer")
        self.root.configure(bg=THEME["bg"])
        self.root.geometry(f"{self.width}x{self.height}")

        main_frame = tk.Frame(self.root, bg=THEME["bg"])
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = tk.Label(
            main_frame,
            text="MPLS (Hackers_tchad) - Protocol Simulation & 3D Visualizer",
            bg=THEME["bg"],
            fg=THEME["accent"],
            font=("Consolas", 18, "bold"),
        )
        header.pack(pady=6)

        # Toolbar
        toolbar = tk.Frame(main_frame, bg=THEME["panel"])
        toolbar.pack(fill=tk.X, padx=8, pady=4)
        for text, cmd in [
            ("Build LDP", self._build_ldp),
            ("Build SR", self._build_sr),
            ("Build Tunnels", self._build_tunnels),
            ("Ping", self._run_ping),
            ("Traceroute", self._run_traceroute),
            ("Animate Packet", self._animate_packet),
            ("Reset View", self._reset_view),
            ("Export LFIB", self._export_lfib),
        ]:
            btn = tk.Button(toolbar, text=text, command=cmd, bg=THEME["panel"],
                            fg=THEME["text"], activebackground=THEME["accent"],
                            font=("Consolas", 10, "bold"))
            btn.pack(side=tk.LEFT, padx=4)

        # Status
        self.status_var = tk.StringVar(value="Ready")
        status = tk.Label(main_frame, textvariable=self.status_var, bg=THEME["bg"],
                          fg=THEME["success"], font=("Consolas", 10))
        status.pack(anchor=tk.W, padx=10)

        # Canvas
        self.canvas = tk.Canvas(main_frame, bg=THEME["bg"], highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Bind interactions
        self.canvas.bind("<ButtonPress-1>", self._on_mouse_down)
        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<MouseWheel>", self._on_wheel)
        self.root.bind("<Key-r>", lambda e: self._reset_view())
        self.root.bind("<Key-q>", lambda e: self.root.destroy())

        self._draw_static_scene()
        self._schedule_refresh()

    def _draw_static_scene(self) -> None:
        self.canvas.delete("all")
        # Grid floor
        for i in range(-10, 11):
            self._draw_grid_line(i, -10, i, 10)
            self._draw_grid_line(-10, i, 10, i)
        # Links
        for link in self.network.links:
            self._draw_link(link)
        # Routers
        for name, router in self.network.routers.items():
            self._draw_router(name, router)

    def _draw_grid_line(self, x1: float, z1: float, x2: float, z2: float) -> None:
        px1, py1, _ = self.project(x1, -2.0, z1)
        px2, py2, _ = self.project(x2, -2.0, z2)
        self.canvas.create_line(px1, py1, px2, py2, fill=THEME["grid"], width=1)

    def _draw_link(self, link: Link) -> None:
        src = self.network.routers.get(link.source)
        dst = self.network.routers.get(link.target)
        if not src or not dst:
            return
        x1, y1, _ = self.project(*src.position)
        x2, y2, _ = self.project(*dst.position)
        line_id = self.canvas.create_line(x1, y1, x2, y2, fill=THEME["edge"], width=2, smooth=True)
        self.edge_lines[(link.source, link.target)] = line_id

    def _draw_router(self, name: str, router: MPLSRouter) -> None:
        px, py, depth = self.project(*router.position)
        size = max(10, min(28, 24 - depth / 80))
        color = THEME["node"]
        if router.is_pes:
            color = THEME["warning"]
        elif router.is_p:
            color = THEME["success"]
        elif router.is_ce:
            color = "#8888ff"
        cid = self.canvas.create_oval(
            px - size, py - size, px + size, py + size,
            fill=color, outline=THEME["node_border"], width=2,
        )
        self.node_circles[name] = cid
        self.canvas.create_text(px, py - size - 12, text=name, fill=THEME["text"],
                                font=("Consolas", 10, "bold"))
        rid = router.router_id
        self.canvas.create_text(px, py + size + 12, text=rid, fill="#8888aa",
                                font=("Consolas", 8))

    def _schedule_refresh(self) -> None:
        if not self.root:
            return
        self._update_animations()
        self.root.after(33, self._schedule_refresh)  # ~30 FPS

    def _update_animations(self) -> None:
        finished = []
        for ap in self.anim_packets:
            ap["progress"] += 0.04
            if ap["progress"] >= 1.0:
                finished.append(ap)
                continue
            src_pos = self.network.routers[ap["src"]].position
            dst_pos = self.network.routers[ap["dst"]].position
            x = src_pos[0] + (dst_pos[0] - src_pos[0]) * ap["progress"]
            y = src_pos[1] + (dst_pos[1] - src_pos[1]) * ap["progress"]
            z = src_pos[2] + (dst_pos[2] - src_pos[2]) * ap["progress"]
            px, py, _ = self.project(x, y, z)
            if ap.get("canvas_id"):
                self.canvas.coords(ap["canvas_id"], px - 6, py - 6, px + 6, py + 6)
        for ap in finished:
            if ap.get("canvas_id"):
                self.canvas.delete(ap["canvas_id"])
            self.anim_packets.remove(ap)

    def _on_mouse_down(self, event) -> None:
        self._drag_start = (event.x, event.y)

    def _on_mouse_drag(self, event) -> None:
        if self._drag_start is None:
            return
        dx = event.x - self._drag_start[0]
        dy = event.y - self._drag_start[1]
        self.rot_y += dx * 0.01
        self.rot_x += dy * 0.01
        self._drag_start = (event.x, event.y)
        self._draw_static_scene()

    def _on_wheel(self, event) -> None:
        delta = event.delta / 120
        self.scale *= 1.1 ** delta
        self._draw_static_scene()

    def _reset_view(self) -> None:
        self.rot_x = 0.45
        self.rot_y = 0.55
        self.scale = 60.0
        self.pan_x = self.width / 2
        self.pan_y = self.height / 2
        self._draw_static_scene()

    def _build_ldp(self) -> None:
        self.network.build_all_ldp()
        self.status_var.set(f"LDP built. Topology v{self.network.topology_version}")

    def _build_sr(self) -> None:
        self.network.build_all_sr()
        self.status_var.set("Segment Routing MPLS LFIB built")

    def _build_tunnels(self) -> None:
        self.network.build_all_tunnels()
        self.status_var.set("RSVP-TE tunnels computed & installed")

    def _run_ping(self) -> None:
        routers = list(self.network.routers.keys())
        if len(routers) < 2:
            return
        src, dst = routers[0], routers[-1]
        res = self.network.ping(src, dst, count=1, callback=lambda n, p: self._flash_node(n))
        ok = res["results"][0]["success"]
        self.status_var.set(f"Ping {src}->{dst}: {'SUCCESS' if ok else 'FAILED'}")

    def _run_traceroute(self) -> None:
        routers = list(self.network.routers.keys())
        if len(routers) < 2:
            return
        src, dst = routers[0], routers[-1]
        res = self.network.traceroute(src, dst)
        hops = " -> ".join(str(h["node"]) for h in res["hops"])
        self.status_var.set(f"Traceroute: {hops}")

    def _animate_packet(self) -> None:
        routers = list(self.network.routers.keys())
        if len(routers) < 2:
            return
        src, dst = routers[0], routers[1]
        px, py, _ = self.project(*self.network.routers[src].position)
        cid = self.canvas.create_oval(px - 6, py - 6, px + 6, py + 6,
                                      fill=THEME["label_stack"], outline=THEME["node_border"])
        self.anim_packets.append({"src": src, "dst": dst, "progress": 0.0, "canvas_id": cid})
        self.status_var.set(f"Animating packet {src}->{dst}")

    def _flash_node(self, name: str) -> None:
        cid = self.node_circles.get(name)
        if cid:
            self.canvas.itemconfig(cid, fill=THEME["accent"])
            self.root.after(150, lambda: self.canvas.itemconfig(cid, fill=THEME["node"]))

    def _export_lfib(self) -> None:
        data = {n: [e.to_dict() for e in r.fwd.lfib.values()] for n, r in self.network.routers.items()}
        with open("lfib_export.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        self.status_var.set("LFIB exported to lfib_export.json")

    def run(self) -> None:
        self.build_ui()
        self.running = True
        self.root.mainloop()
        self.running = False


# ############################################################################
# SECTION 7: SAMPLE TOPOLOGIES & CLI
# ############################################################################

def sample_mpls_topology() -> MPLSNetwork:
    """Create a realistic MPLS core topology."""
    net = MPLSNetwork()
    routers = [
        ("PE1", -6.0, 0.0, -3.0, True, False, False),
        ("P1", -2.0, 0.0, -1.0, False, True, False),
        ("P2", 2.0, 0.0, -1.0, False, True, False),
        ("P3", 0.0, 2.0, 1.0, False, True, False),
        ("PE2", 6.0, 0.0, -3.0, True, False, False),
        ("CE1", -9.0, 0.0, -5.0, False, False, True),
        ("CE2", 9.0, 0.0, -5.0, False, False, True),
    ]
    for name, x, y, z, is_pe, is_p, is_ce in routers:
        r = MPLSRouter(name, x, y, z)
        r.is_pes = is_pe
        r.is_p = is_p
        r.is_ce = is_ce
        r.ldp_enabled = True
        r.rsvp_enabled = not is_ce
        r.sr_enabled = not is_ce
        r.bgp_enabled = is_pe
        if not is_ce:
            r.add_interface(Interface(name="Lo0", ip=generate_router_id(name), mpls_enabled=True))
            r.add_interface(Interface(name="Gi0/0/0", mpls_enabled=True))
            r.add_interface(Interface(name="Gi0/0/1", mpls_enabled=True))
            r.sr_prefix_sid = 16000 + hash(name) % 1000
        else:
            r.add_interface(Interface(name="Gi0", mpls_enabled=False))
        net.add_router(r)

    links = [
        ("PE1", "P1", "Gi0/0/0", "Gi0/0/0", 10),
        ("P1", "P2", "Gi0/0/1", "Gi0/0/0", 10),
        ("P2", "PE2", "Gi0/0/1", "Gi0/0/0", 10),
        ("P1", "P3", "Gi0/0/2", "Gi0/0/0", 15),
        ("P3", "P2", "Gi0/0/1", "Gi0/0/2", 15),
        ("CE1", "PE1", "Gi0", "Gi0/0/2", 100),
        ("CE2", "PE2", "Gi0", "Gi0/0/2", 100),
    ]
    for a, b, ai, bi, metric in links:
        net.add_link(Link(source=a, target=b, source_intf=ai, target_intf=bi, metric=metric))
        net.add_link(Link(source=b, target=a, source_intf=bi, target_intf=ai, metric=metric))

    # Add a tunnel on PE1
    tunnel = Tunnel(name="TUN_PE1_PE2", headend="PE1", tailend="PE2",
                    style=TunnelStyle.CSPF, bandwidth=100000, protection=ProtectionType.LINK_PROTECTION)
    net.routers["PE1"].tunnels[tunnel.name] = tunnel

    return net


def cli_main() -> None:
    parser = argparse.ArgumentParser(description="MPLS (Hackers_tchad) Advanced Simulator")
    parser.add_argument("--gui", action="store_true", help="Launch 3D Tkinter visualizer")
    parser.add_argument("--build", action="store_true", help="Build LDP LFIB and print JSON")
    parser.add_argument("--ping", nargs=2, metavar=("SRC", "DST"), help="Run MPLS ping")
    parser.add_argument("--trace", nargs=2, metavar=("SRC", "DST"), help="Run MPLS traceroute")
    parser.add_argument("--export", type=str, default="mpls_topology.json", help="Export topology JSON")
    args = parser.parse_args()

    net = sample_mpls_topology()
    net.build_all_ldp()
    net.build_all_sr()
    net.build_all_tunnels()

    if args.ping:
        res = net.ping(args.ping[0], args.ping[1])
        print(indent_json(res))
    if args.trace:
        res = net.traceroute(args.trace[0], args.trace[1])
        print(indent_json(res))
    if args.export:
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(net.to_dict(), f, indent=2)
        print(f"Topology exported to {args.export}")
    if args.build:
        print(indent_json(net.to_dict()))
    if args.gui or not any([args.build, args.ping, args.trace]):
        vis = MPLSVisualizer3D(net)
        vis.run()


if __name__ == "__main__":
    cli_main()
