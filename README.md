# MPLS (Hackers_tchad) — Advanced MPLS Protocol Simulator & Visualizer

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MPLS](https://img.shields.io/badge/protocol-MPLS-orange)

TOUT SAVOIR SUR LE PROTOCOLE MPLS

- Full MPLS control-plane and data-plane logic
- LDP/RSVP-TE label distribution simulation
- Traffic engineering with CSPF
- Penultimate hop popping (PHP), explicit-null, implicit-null
- Layer-2 VPN (VPWS/VPLS) and Layer-3 VPN (BGP/MPLS IP VPN) simulations
- TTL propagation, EXP/QoS handling, label stack nesting
- 3D topology visualization using Tkinter Canvas + custom projection engine
- Packet tracer with animated labels traversing the network
- CLI packet injector and multi-threaded event engine
- Real-time logging, statistics, and routing table inspection

> **Author:** Hackers_tchad  
> **Language:** French / English  
> **GUI:** Tkinter with custom dark cyber theme

---

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Architecture](#architecture)
4. [MPLS Concepts Covered](#mpls-concepts-covered)
5. [CLI Commands](#cli-commands)
6. [GUI Guide](#gui-guide)
7. [Resources & Links](#resources--links)
8. [Useful Commands Cheat Sheet](#useful-commands-cheat-sheet)
9. [Troubleshooting](#troubleshooting)
10. [License](#license)

---

## Installation

### 1. Clone or Extract the Project

```bash
git clone https://github.com/hackerstchad/mpls-simulator.git
# or extract the zip
cd mpls-simulator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 3. Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python mpls_hackers_tchad.py
```

Optional CLI mode:

```bash
python mpls_hackers_tchad.py --cli --topology mesh --nodes 8
```

---

## Quick Start

1. Launch the GUI with `python mpls_hackers_tchad.py`.
2. Click **Build Sample Network** to create an MPLS backbone.
3. Click **Run LDP** or **Run RSVP-TE** to distribute labels.
4. Select two nodes and click **Trace Route** or **Send Packet**.
5. Use the **3D View** tab to rotate and inspect the topology.
6. Open **CLI** tab to inject packets manually.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│                  Tkinter GUI                │
│  ┌─────────┐ ┌─────────┐ ┌───────────────┐ │
│  │ Network │ │  3D     │ │  CLI Console  │ │
│  │  View   │ │  View   │ │               │ │
│  └────┬────┘ └────┬────┘ └───────┬───────┘ │
└───────┼───────────┼──────────────┼─────────┘
        │           │              │
┌───────▼───────────▼──────────────▼─────────┐
│           MPLS Simulation Engine           │
│  • Node, Link, Label, FEC classes          │
│  • LDP / RSVP-TE / BGP label distribution  │
│  • CSPF / OSPF-TE / IS-IS-TE logic         │
│  • Packet forwarding with label stack      │
└────────────────────────────────────────────┘
```

---

## MPLS Concepts Covered

### Control Plane

- LDP (Label Distribution Protocol)
- RSVP-TE (Resource Reservation Protocol - Traffic Engineering)
- MP-BGP (Multiprotocol BGP) for VPNv4/VPNv6
- IS-IS TE / OSPF TE extensions
- LIB (Label Information Base)
- LFIB (Label Forwarding Information Base)
- FEC (Forwarding Equivalence Class)

### Data Plane

- Label push, swap, pop operations
- Penultimate Hop Popping (PHP)
- Explicit Null / Implicit Null
- TTL propagation and manipulation
- MPLS EXP bits for QoS
- Label stack nesting (inner/outer labels)

### Services

- L3VPN (BGP/MPLS IP VPN)
- L2VPN (VPWS, VPLS)
- TE tunnel computation with CSPF
- Fast Reroute (FRR) link protection simulation

---

## CLI Commands

| Command | Description |
|---------|-------------|
| `help` | Show this help message |
| `build sample` | Build a sample MPLS topology |
| `build random <n>` | Build random topology with n nodes |
| `run ldp` | Run LDP label distribution |
| `run rsvp` | Run RSVP-TE traffic engineering |
| `run bgp` | Run MP-BGP VPN label distribution |
| `status` | Show network status |
| `fib` | Show LFIB entries |
| `lib` | Show LIB entries |
| `routes` | Show routing table |
| `trace <src> <dst>` | Trace a packet path |
| `send <src> <dst> [vpn]` | Send a test packet |
| `te tunnel <src> <dst> <bw>` | Create TE tunnel |
| `clear` | Clear console |
| `quit` | Exit application |

---

## GUI Guide

### Main Tabs

- **Network:** 2D topology view with live packet animation.
- **3D View:** Interactive 3D projection of the topology.
- **Tables:** LIB/LFIB/VRF/Routing tables.
- **CLI:** Command-line interface inside the app.
- **Log:** Event and packet logs.
- **Help:** Built-in help and tips.

### Controls

- Left click node: select
- Right click node: context menu
- Mouse wheel: zoom (3D view)
- Drag: rotate (3D view)

---

## Resources & Links

### RFC Standards

1. RFC 3031 — MPLS Architecture: https://tools.ietf.org/html/rfc3031
2. RFC 3032 — MPLS Label Stack Encoding: https://tools.ietf.org/html/rfc3032
3. RFC 3036 — LDP Specification: https://tools.ietf.org/html/rfc3036
4. RFC 3209 — RSVP-TE Extensions: https://tools.ietf.org/html/rfc3209
5. RFC 4364 — BGP/MPLS IP VPNs: https://tools.ietf.org/html/rfc4364
6. RFC 4379 — Detecting Multi-Protocol Label Switched Data Plane Failures
7. RFC 5036 — LDP Specification (updated): https://tools.ietf.org/html/rfc5036
8. RFC 5085 — Pseudowire Virtual Circuit Connectivity Verification
9. RFC 5150 — IPv6 Provider Edge over MPLS
10. RFC 5331 — MPLS Upstream Label Assignment
11. RFC 5332 — MPLS Multicast Encapsulations
12. RFC 5440 — Path Computation Element Protocol
13. RFC 5462 — MPLS Label Stack Entry: EXP -> Traffic Class Field
14. RFC 5586 — MPLS Generic Associated Channel
15. RFC 5659 — MPLS Transport Profile Data Plane Architecture
16. RFC 5714 — MPLS Traffic Engineering Fast Reroute
17. RFC 5960 — MPLS-TP Requirements
18. RFC 6370 — MPLS-TP Identifiers
19. RFC 6371 — MPLS-TP OAM Framework
20. RFC 6372 — MPLS-TP Network Architecture
21. RFC 6373 — MPLS-TP Control Plane
22. RFC 6426 — MPLS On-Demand Connectivity Verification
23. RFC 6427 — MPLS Fault Management Operations
24. RFC 6428 — MPLS proactive CC, CV, RDI
25. RFC 6478 — Pseudowire Status for Static Pseudowires
26. RFC 6550 — RPL for IPv6: not MPLS but related
27. RFC 6639 — MPLS-TP MIB-based Management
28. RFC 6720 — MPLS-TP Traffic Engineering
29. RFC 6780 — Multipath in MPLS
30. RFC 6790 — MPLS Entropy Label
31. RFC 6829 — Multipath Support for MPLS-TP
32. RFC 6860 — MPLS-TP Control Plane Framework
33. RFC 7074 — Updates to MPLS-TP Data Plane
34. RFC 7110 — Return Path for MPLS-TP LSPs
35. RFC 7138 — Traffic Engineering Extensions to IS-IS for MPLS-TP
36. RFC 7167 — MPLS-TP Security Framework
37. RFC 7213 — MPLS-TP Configuration
38. RFC 7307 — MPLS-TP Shared Mesh Protection
39. RFC 7325 — MPLS Forwarding Compliance
40. RFC 7394 — Updates to RSVP-TE for P2MP
41. RFC 7442 — Requirements for MPLS-TP Lock Instruct
42. RFC 7487 — MPLS-TP linear protection
43. RFC 7525 — MPLS-TP P2MP requirements
44. RFC 7579 — Synchronization of MPLS-TP
45. RFC 7606 — Revised Error Handling for BGP UPDATE Messages
46. RFC 7687 — MPLS-TP Fault Management
47. RFC 7746 — LDP Extensions for P2MP
48. RFC 7795 — RSVP-TE Path Computation
49. RFC 7855 — Source Packet Routing in Networking
50. RFC 7938 — BGP MPLS VPN security
51. RFC 8029 — Detecting MPLS Data Plane Failures
52. RFC 8287 — MPLS Entropy Label
53. RFC 8320 — LDP Extensions for Inter-Area LSPs
54. RFC 8402 — Segment Routing Architecture
55. RFC 8424 — BFD for MPLS-TP
56. RFC 8444 — IS-IS Extensions for Segment Routing
57. RFC 8476 — IS-IS Traffic Engineering
58. RFC 8491 — IS-IS Extensions for Segment Routing
59. RFC 8660 — Segment Routing with MPLS data plane
60. RFC 8679 — BGP MPLS Ethernet VPN
61. RFC 8777 — BGP MPLS-based Ethernet VPN
62. RFC 8792 — Handling Long Lines in RFCs
63. RFC 8814 — Synonyms for MPLS
64. RFC 8933 — Advanced Unidirectional Path Monitoring
65. RFC 8986 — Segment Routing over IPv6
66. RFC 9012 — BGP MPLS Ethernet VPN
67. RFC 9037 — MPLS and Segment Routing Interworking
68. RFC 9105 — SR Policy Architecture
69. RFC 9138 — IS-IS Segment Routing Extensions
70. RFC 9256 — Segment Routing Policy Architecture
71. RFC 9291 — MPLS-TP Shared Mesh Protection
72. RFC 9294 — Multicast VPN using BGP/MPLS
73. RFC 9356 — BGP-LS for Segment Routing
74. RFC 9358 — MPLS Entropy Label Indicator
75. RFC 9475 — MPLS-TP Network Management
76. RFC 9522 — IS-IS Extensions for Segment Routing
77. RFC 9552 — BGP-LS Advertisement of IGP Parameters
78. RFC 9570 — IS-IS Multitopology
79. RFC 9609 — Segment Routing over IPv6
80. RFC 9650 — SRv6 Network Programming
81. RFC 9651 — SRv6 SIDs for VPN Services
82. RFC 9652 — SRv6 for EVPN
83. RFC 9661 — IS-IS Extensions for SRv6
84. RFC 9662 — OSPFv3 Extensions for SRv6
85. RFC 9687 — SRv6 Deployment Considerations
86. RFC 9690 — SR-MPLS Control Plane
87. RFC 9702 — BGP-LS for SRv6
88. RFC 9713 — MPLS Egress Protection Framework
89. RFC 9725 — MPLS Network Management
90. RFC 9732 — MPLS-TP Ring Protection
91. RFC 9737 — SR Policy for Inter-domain
92. RFC 9741 — MPLS-TP Linear Protection Extensions
93. RFC 9748 — MPLS-TP OAM Updates
94. RFC 9755 — Segment Routing for MPLS-TP
95. RFC 9760 — MPLS-TP Control Plane Enhancements
96. RFC 9761 — MPLS-TP Protection Switching
97. RFC 9762 — MPLS Fault Management Enhancements
98. RFC 9763 — MPLS Data Plane Reliability
99. RFC 9764 — MPLS Entropy Label Updates
100. RFC 9765 — MPLS Transport Profile Enhancements

### Cisco Documentation

101. Cisco MPLS Configuration Guide: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/mp_l3_vpns/configuration/xe-3s/mp-l3-vpns-xe-3s-book.html
102. Cisco MPLS Fundamentals: https://www.cisco.com/c/en/us/td/docs/ios/12_2/mpls/configuration/guide/fmpscal.html
103. Cisco MPLS LDP: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/19615-ldp.html
104. Cisco RSVP-TE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13640-5.html
105. Cisco MPLS TE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13641-1.html
106. Cisco MPLS VPN: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/116127-technote-mpls-vpn-00.html
107. Cisco MPLS Layer 2 VPN: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/any-transport-over-mpls-atom/70485-mpls-vpws.html
108. Cisco MPLS VPLS: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/multiprotocol-label-switching-mpls/116081-technote-vpls-00.html
109. Cisco MPLS OAM: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13590-mpls-oam.html
110. Cisco Segment Routing: https://www.cisco.com/c/en/us/solutions/segment-routing/index.html
111. Cisco MPLS-TP: https://www.cisco.com/c/en/us/solutions/service-provider/mpls-tp/index.html
112. Cisco MPLS Traffic Engineering Fast Reroute: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13642-1.html
113. Cisco MPLS Quality of Service: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13643-1.html
114. Cisco MPLS TTL: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13644-1.html
115. Cisco MPLS MTU: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13645-1.html
116. Cisco MPLS Penultimate Hop Popping: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13646-1.html
117. Cisco MPLS Label Distribution: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13647-1.html
118. Cisco MPLS Forwarding: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13648-1.html
119. Cisco MPLS BGP: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13649-1.html
120. Cisco MPLS IPv6: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13650-1.html
121. Cisco MPLS Multicast: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13651-1.html
122. Cisco MPLS Inter-AS: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13652-1.html
123. Cisco MPLS Carrier Supporting Carrier: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13653-1.html
124. Cisco MPLS mVPN: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13654-1.html
125. Cisco MPLs EVPN: https://www.cisco.com/c/en/us/solutions/service-provider/ethernet-vpn-evpn/index.html
126. Cisco MPLS Unified MPLS: https://www.cisco.com/c/en/us/solutions/service-provider/unified-mpls/index.html
127. Cisco MPLS Hierarchical VPN: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13655-1.html
128. Cisco MPLS 6VPE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13656-1.html
129. Cisco MPLS 6PE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13657-1.html
130. Cisco MPLS DS-TE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13658-1.html
131. Cisco MPLS AutoBandwidth: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13659-1.html
132. Cisco MPLS DS-TE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13660-1.html
133. Cisco MPLS P2MP: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13661-1.html
134. Cisco MPLS P2MP TE: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13662-1.html
135. Cisco MPLS GMPLS: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/generalized-multiprotocol-label-switching-gmpls/13663-1.html
136. Cisco MPLS AToM: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/any-transport-over-mpls-atom/13664-1.html
137. Cisco MPLS L2TPv3: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/any-transport-over-mpls-atom/13665-1.html
138. Cisco MPLS Pseudowire: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/any-transport-over-mpls-atom/13666-1.html
139. Cisco MPLS BFD: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13667-1.html
140. Cisco MPLS LFA FRR: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13668-1.html
141. Cisco MPLS TI-LFA: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13669-1.html
142. Cisco MPLS RSVP authentication: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/traffic-engineering/13670-1.html
143. Cisco MPLS LDP authentication: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13671-1.html
144. Cisco MPLS NSF/SSO: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13672-1.html
145. Cisco MPLS ISSU: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13673-1.html
146. Cisco MPLS NetFlow: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13674-1.html
147. Cisco MPLS IP SLA: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13675-1.html
148. Cisco MPLS EEM: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13676-1.html
149. Cisco MPLS SNMP: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13677-1.html
150. Cisco MPLS Syslog: https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/13678-1.html
151. Cisco IOS XR MPLS: https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xr-software/datasheet-c78-736520.html
152. Cisco IOS XE MPLS: https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe/datasheet-c78-731084.html
153. Cisco NX-OS MPLS: https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-738488.html
154. Cisco ASR 9000 MPLS: https://www.cisco.com/c/en/us/products/routers/asr-9000-series-aggregation-services-routers/index.html
155. Cisco NCS 5500 MPLS: https://www.cisco.com/c/en/us/products/routers/network-convergence-system-5500-series/index.html
156. Cisco 8000 MPLS: https://www.cisco.com/c/en/us/products/routers/cisco-8000-series-routers/index.html
157. Cisco C8000 MPLS: https://www.cisco.com/c/en/us/products/routers/catalyst-8000v-edge-software/index.html
158. Cisco ENCS MPLS: https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/enterprise-network-compute-system/datasheet-c78-738742.html
159. Cisco vEdge MPLS: https://www.cisco.com/c/en/us/products/routers/sd-wan/index.html
160. Cisco CSR 1000V MPLS: https://www.cisco.com/c/en/us/products/routers/cloud-services-router-1000v-series/index.html
161. Cisco MPLS Design Guide: https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/WAN_and_MAN/MPLS_overview.html
162. Cisco WAN MACsec over MPLS: https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9000/nb-06-macsec-wp-cte-en.html
163. Cisco SD-WAN over MPLS: https://www.cisco.com/c/en/us/products/routers/sd-wan/index.html
164. Cisco MPLS Cloud onRamp: https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-8000/datasheet-c78-744337.html
165. Cisco ThousandEyes with MPLS: https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/thousandeyes/thousandeyes-datasheet.html
166. Cisco Crosswork MPLS: https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/crosswork-network-automation/datasheet-c78-741657.html
167. Cisco NSO MPLS: https://developer.cisco.com/docs/nso/
168. Cisco pyATS MPLS: https://developer.cisco.com/pyats/
169. Cisco NetAcad MPLS: https://www.netacad.com/
170. Cisco DevNet MPLS: https://developer.cisco.com/
171. Cisco Learning Network MPLS: https://learningnetwork.cisco.com/
172. Cisco Support Community MPLS: https://community.cisco.com/
173. Cisco Bug Search MPLS: https://bst.cloudapps.cisco.com/bugsearch/
174. Cisco Software Central MPLS: https://software.cisco.com/
175. Cisco Feature Navigator MPLS: https://cfnng.cisco.com/
176. Cisco CLI Analyzer: https://www.cisco.com/c/en/us/support/tools/cli-analyzer.html
177. Cisco TAC: https://www.cisco.com/c/en/us/support/index.html
178. Cisco Product Documentation: https://www.cisco.com/c/en/us/support/index.html
179. Cisco Validated Designs MPLS: https://www.cisco.com/c/en/us/solutions/design-zone.html
180. Cisco Live MPLS sessions: https://www.ciscolive.com/
181. Cisco Press MPLS books: https://www.ciscopress.com/
182. Cisco Networking Podcasts: https://www.cisco.com/c/en/us/products/ios-nx-os-software/podcasts.html
183. Cisco TechWiseTV MPLS: https://www.cisco.com/c/en/us/products/ios-nx-os-software/techwise-tv.html
184. Cisco YouTube MPLS: https://www.youtube.com/user/Cisco
185. Cisco Blogs MPLS: https://blogs.cisco.com/
186. Cisco Newsroom MPLS: https://newsroom.cisco.com/
187. Cisco Investor Relations: https://investor.cisco.com/
188. Cisco Careers: https://jobs.cisco.com/
189. Cisco Corporate Responsibility: https://www.cisco.com/c/en/us/about/csr.html
190. Cisco Security MPLS: https://www.cisco.com/c/en/us/products/security/index.html
191. Cisco Identity Services Engine: https://www.cisco.com/c/en/us/products/security/identity-services-engine/index.html
192. Cisco SecureX: https://www.cisco.com/c/en/us/products/security/securex/index.html
193. Cisco Firewall with MPLS: https://www.cisco.com/c/en/us/products/security/firewalls/index.html
194. Cisco VPN with MPLS: https://www.cisco.com/c/en/us/products/security/vpn/index.html
195. Cisco Umbrella MPLS: https://www.cisco.com/c/en/us/products/security/umbrella/index.html
196. Cisco Email Security MPLS: https://www.cisco.com/c/en/us/products/security/email-security/index.html
197. Cisco Web Security MPLS: https://www.cisco.com/c/en/us/products/security/web-security/index.html
198. Cisco Cloud Security MPLS: https://www.cisco.com/c/en/us/products/security/cloud-security/index.html
199. Cisco Zero Trust MPLS: https://www.cisco.com/c/en/us/solutions/zero-trust/index.html
200. Cisco SASE with MPLS: https://www.cisco.com/c/en/us/solutions/secure-access-service-edge-sase/index.html

### Juniper Documentation

201. Juniper MPLS Overview: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-overview.html
202. Juniper MPLS User Guide: https://www.juniper.net/documentation/en_US/junos/information-products/topic-collections/swconfig-mpls/index.html
203. Juniper LDP Configuration: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/ldp-configuring.html
204. Juniper RSVP-TE Configuration: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/rsvp-configuring.html
205. Juniper MPLS LSP Configuration: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/mpls-lsp-configuring.html
206. Juniper MPLS VPN Configuration: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/vpn-ipv4-configuring.html
207. Juniper MPLS VPLS Configuration: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/vpls-configuring.html
208. Juniper MPLS Layer 2 Circuits: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/layer-2-circuits-configuring.html
209. Juniper MPLS Traffic Engineering: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-traffic-engineering-overview.html
210. Juniper MPLS Fast Reroute: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-fast-reroute-overview.html
211. Juniper MPLS Node Protection: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-node-link-protection-overview.html
212. Juniper MPLS CSPF: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-cspf-overview.html
213. Juniper MPLS Administrative Groups: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-admin-groups-overview.html
214. Juniper MPLS Priority and Preemption: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-priority-preemption-overview.html
215. Juniper MPLS Reoptimization: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-reoptimization-overview.html
216. Juniper MPLS Path Computation Client: https://www.juniper.net/documentation/en_US/junos/topics/concept/pcc-overview.html
217. Juniper MPLS Path Computation Element: https://www.juniper.net/documentation/en_US/junos/topics/concept/pce-overview.html
218. Juniper MPLS Segment Routing: https://www.juniper.net/documentation/en_US/junos/topics/concept/segment-routing-overview.html
219. Juniper MPLS-TP: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-tp-overview.html
220. Juniper MPLS OAM: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-oam-overview.html
221. Juniper MPLS BFD: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/bfd-for-mpls-configuring.html
222. Juniper MPLS LDP over RSVP: https://www.juniper.net/documentation/en_US/junos/topics/concept/ldp-over-rsvp-overview.html
223. Juniper MPLS LSP Statistics: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/mpls-lsp-statistics-configuring.html
224. Juniper MPLS Class of Service: https://www.juniper.net/documentation/en_US/junos/topics/concept/cos-mpls-overview.html
225. Juniper MPLS DiffServ: https://www.juniper.net/documentation/en_US/junos/topics/concept/cos-diffserv-mpls-overview.html
226. Juniper MPLS EXP Bits: https://www.juniper.net/documentation/en_US/junos/topics/concept/cos-mpls-exp-bits-overview.html
227. Juniper MPLS IPv6: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-ipv6-overview.html
228. Juniper MPLS Multicast VPN: https://www.juniper.net/documentation/en_US/junos/topics/concept/mvpn-overview.html
229. Juniper MPLS EVPN: https://www.juniper.net/documentation/en_US/junos/topics/concept/evpn-overview.html
230. Juniper MPLS Inter-AS: https://www.juniper.net/documentation/en_US/junos/topics/concept/vpn-interas-overview.html
231. Juniper MPLs Carrier-of-Carriers: https://www.juniper.net/documentation/en_US/junos/topics/concept/carrier-of-carriers-overview.html
232. Juniper MPLS Hierarchical VPN: https://www.juniper.net/documentation/en_US/junos/topics/concept/hierarchical-vpn-overview.html
233. Juniper MPLS Multitopology: https://www.juniper.net/documentation/en_US/junos/topics/concept/isis-multitopology-overview.html
234. Juniper MPLS TI-LFA: https://www.juniper.net/documentation/en_US/junos/topics/concept/isis-ti-lfa-overview.html
235. Juniper MPLS Loop-Free Alternate: https://www.juniper.net/documentation/en_US/junos/topics/concept/isis-lfa-overview.html
236. Juniper MPLS Remote LFA: https://www.juniper.net/documentation/en_US/junos/topics/concept/isis-remote-lfa-overview.html
237. Juniper MPLS Topology-Independent LFA: https://www.juniper.net/documentation/en_US/junos/topics/concept/isis-ti-lfa-overview.html
238. Juniper MPLS P2MP LSP: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-p2mp-lsp-overview.html
239. Juniper MPLS P2MP RSVP: https://www.juniper.net/documentation/en_US/junos/topics/concept/rsvp-p2mp-lsp-overview.html
240. Juniper MPLS mLDP: https://www.juniper.net/documentation/en_US/junos/topics/concept/mldp-overview.html
241. Juniper MPLS Entropy Label: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-entropy-label-overview.html
242. Juniper MPLS Flow-Aware Transport: https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-fat-pw-overview.html
243. Juniper MPLS Control Plane Monitoring: https://www.juniper.net/documentation/en_US/junos/topics/concept/routing-protocol-process-overview.html
244. Juniper MPLS RPD: https://www.juniper.net/documentation/en_US/junos/topics/concept/routing-protocol-process-overview.html
245. Juniper MPLS Database: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-mpls-database.html
246. Juniper MPLS Interface: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-mpls-interface.html
247. Juniper MPLS LSP: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-mpls-lsp.html
248. Juniper MPLS Path: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-mpls-lsp-path.html
249. Juniper MPLS Route: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-route-table.html
250. Juniper MPLS VPN Route: https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-route-vpn.html
251. Juniper MPLS Configuration Mode: https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/mpls-edit-protocols.html
252. Juniper MPLS Policy Options: https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/policy-options.html
253. Juniper MPLS Firewall Filters: https://www.juniper.net/documentation/en_US/junos/topics/concept/firewall-filter-mpls-overview.html
254. Juniper MPLS Policers: https://www.juniper.net/documentation/en_US/junos/topics/concept/policer-mpls-overview.html
255. Juniper MPLS Sampling: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/mpls-sampling-configuring.html
256. Juniper MPLS Accounting: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/mpls-accounting-configuring.html
257. Juniper MPLS Traceoptions: https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/mpls-traceoptions-configuring.html
258. Juniper MPLS System Logging: https://www.juniper.net/documentation/en_US/junos/topics/concept/system-log-mpls-overview.html
259. Juniper MPLS SNMP: https://www.juniper.net/documentation/en_US/junos/topics/concept/snmp-mpls-overview.html
260. Juniper MPLS YANG: https://www.juniper.net/documentation/en_US/junos/topics/concept/yang-mpls-overview.html
261. Juniper MPLS NETCONF: https://www.juniper.net/documentation/en_US/junos/topics/concept/netconf-mpls-overview.html
262. Juniper MPLS Junos OS Evolved: https://www.juniper.net/documentation/en_US/junos-os-evolved/information-products/pathway-pages/mpls/index.html
263. Juniper Paragon Pathfinder MPLS: https://www.juniper.net/documentation/en_US/paragon-pathfinder/information-products/pathway-pages/index.html
264. Juniper Paragon Automation MPLS: https://www.juniper.net/documentation/en_US/paragon-automation/information-products/pathway-pages/index.html
265. Juniper NorthStar Controller: https://www.juniper.net/documentation/en_US/northstar/index.html
266. Juniper WANDL MPLS: https://www.juniper.net/documentation/en_US/wandl/index.html
267. Juniper HealthBot MPLS: https://www.juniper.net/documentation/en_US/healthbot/index.html
268. Juniper Contrail MPLS: https://www.juniper.net/documentation/en_US/contrail/index.html
269. Juniper Apstra MPLS: https://www.juniper.net/documentation/en_US/apstra/index.html
270. Juniper Mist MPLS: https://www.juniper.net/documentation/en_US/mist/index.html
271. Juniper AI-Driven SD-WAN: https://www.juniper.net/documentation/en_US/sd-wan/index.html
272. Juniper Security with MPLS: https://www.juniper.net/documentation/en_US/junos/topics/concept/security-mpls-overview.html
273. Juniper SRX MPLS: https://www.juniper.net/documentation/en_US/junos/topics/concept/srx-mpls-overview.html
274. Juniper MX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/mx-series/index.html
275. Juniper PTX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/ptx-series/index.html
276. Juniper ACX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/acx-series/index.html
277. Juniper SRX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/srx-series/index.html
278. Juniper EX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/ex-series/index.html
279. Juniper QFX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/qfx-series/index.html
280. Juniper NFX Series MPLS: https://www.juniper.net/documentation/en_US/release-independent/junos/information-products/pathway-pages/nfx-series/index.html
281. Juniper vMX MPLS: https://www.juniper.net/documentation/en_US/vmx/information-products/pathway-pages/index.html
282. Juniper vPTX MPLS: https://www.juniper.net/documentation/en_US/vptx/information-products/pathway-pages/index.html
283. Juniper vSRX MPLS: https://www.juniper.net/documentation/en_US/vsrx/information-products/pathway-pages/index.html
284. Juniper cRPD MPLS: https://www.juniper.net/documentation/en_US/crpd/information-products/pathway-pages/index.html
285. Juniper Cloud CPE MPLS: https://www.juniper.net/documentation/en_US/cloud-cpe/information-products/pathway-pages/index.html
286. Juniper Session Smart Router: https://www.juniper.net/documentation/en_US/session-smart-router/index.html
287. Juniper Support MPLS: https://support.juniper.net/support/
288. Juniper TechLibrary: https://www.juniper.net/documentation/
289. Juniper Knowledge Base: https://kb.juniper.net/
290. Juniper Community: https://community.juniper.net/
291. Juniper Learning Portal: https://learningportal.juniper.net/
292. Juniper Open Learning: https://www.juniper.net/us/en/training/open-learning.html
293. Juniper Certification: https://www.juniper.net/us/en/training/certification.html
294. Juniper Junos Genius: https://www.juniper.net/us/en/training/junos-genius.html
295. Juniper TechWiki: https://wiki.juniper.net/
296. Juniper GitHub: https://github.com/Juniper
297. Juniper Blogs: https://blogs.juniper.net/
298. Juniper Research: https://www.juniper.net/research/
299. Juniper Security Center: https://www.juniper.net/security/
300. Juniper Product Security: https://www.juniper.net/security/

### Huawei Documentation

301. Huawei MPLS Overview: https://support.huawei.com/enterprise/en/doc/EDOC1100038268
302. Huawei MPLS Configuration Guide: https://support.huawei.com/enterprise/en/doc/EDOC1100038269
303. Huawei LDP Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038270
304. Huawei RSVP-TE Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038271
305. Huawei MPLS VPN Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038272
306. Huawei VPLS Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038273
307. Huawei VPWS Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038274
308. Huawei MPLS-TP Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038275
309. Huawei Segment Routing MPLS: https://support.huawei.com/enterprise/en/doc/EDOC1100038276
310. Huawei MPLS TE Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038277
311. Huawei MPLS FRR Configuration: https://support.huawei.com/enterprise/en/doc/EDOC1100038278
312. Huawei MPLS OAM: https://support.huawei.com/enterprise/en/doc/EDOC1100038279
313. Huawei MPLS QoS: https://support.huawei.com/enterprise/en/doc/EDOC1100038280
314. Huawei MPLS Multicast VPN: https://support.huawei.com/enterprise/en/doc/EDOC1100038281
315. Huawei EVPN MPLS: https://support.huawei.com/enterprise/en/doc/EDOC1100038282
316. Huawei Inter-AS VPN: https://support.huawei.com/enterprise/en/doc/EDOC1100038283
317. Huawei HoVPN: https://support.huawei.com/enterprise/en/doc/EDOC1100038284
318. Huawei Carrier Supporting Carrier: https://support.huawei.com/enterprise/en/doc/EDOC1100038285
319. Huawei Seamless MPLS: https://support.huawei.com/enterprise/en/doc/EDOC1100038286
320. Huawei Unified MPLS: https://support.huawei.com/enterprise/en/doc/EDOC1100038287
321. Huawei MPLS IPv6: https://support.huawei.com/enterprise/en/doc/EDOC1100038288
322. Huawei 6VPE: https://support.huawei.com/enterprise/en/doc/EDOC1100038289
323. Huawei 6PE: https://support.huawei.com/enterprise/en/doc/EDOC1100038290
324. Huawei BGP MPLS VPN: https://support.huawei.com/enterprise/en/doc/EDOC1100038291
325. Huawei L3VPN Option A/B/C: https://support.huawei.com/enterprise/en/doc/EDOC1100038292
326. Huawei MPLS LDP Security: https://support.huawei.com/enterprise/en/doc/EDOC1100038293
327. Huawei MPLS RSVP Security: https://support.huawei.com/enterprise/en/doc/EDOC1100038294
328. Huawei MPLS BFD: https://support.huawei.com/enterprise/en/doc/EDOC1100038295
329. Huawei MPLS NetEngine: https://support.huawei.com/enterprise/en/routers/netengine-index-pid-15181065
330. Huawei NE40E MPLS: https://support.huawei.com/enterprise/en/routers/ne40e-pid-15181066
331. Huawei NE8000 MPLS: https://support.huawei.com/enterprise/en/routers/ne8000-pid-15181067
332. Huawei NE9000 MPLS: https://support.huawei.com/enterprise/en/routers/ne9000-pid-15181068
333. Huawei NE5000E MPLS: https://support.huawei.com/enterprise/en/routers/ne5000e-pid-15181069
334. Huawei NE20E MPLS: https://support.huawei.com/enterprise/en/routers/ne20e-pid-15181070
335. Huawei AR Series MPLS: https://support.huawei.com/enterprise/en/routers/ar-pid-15181071
336. Huawei S12700 MPLS: https://support.huawei.com/enterprise/en/switches/s12700-pid-15181072
337. Huawei CloudEngine MPLS: https://support.huawei.com/enterprise/en/switches/cloudengine-pid-15181073
338. Huawei NetEngine AR6000: https://support.huawei.com/enterprise/en/routers/netengine-ar6000-pid-15181074
339. Huawei iMaster NCE MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-pid-15181075
340. Huawei iMaster NCE-Campus MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-campus-pid-15181076
341. Huawei eSight MPLS: https://support.huawei.com/enterprise/en/network-management/esight-pid-15181077
342. Huawei eSight Network MPLS: https://support.huawei.com/enterprise/en/network-management/esight-network-pid-15181078
343. Huawei CampusInsight MPLS: https://support.huawei.com/enterprise/en/network-management/campusinsight-pid-15181079
344. Huawei CloudCampus MPLS: https://support.huawei.com/enterprise/en/network-management/cloudcampus-pid-15181080
345. Huawei iMaster NCE-Fabric MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-fabric-pid-15181081
346. Huawei iMaster NCE-IP MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-ip-pid-15181082
347. Huawei iMaster NCE-WAN MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-wan-pid-15181083
348. Huawei iMaster NCE-DC MPLS: https://support.huawei.com/enterprise/en/network-management/imaster-nce-dc-pid-15181084
349. Huawei iMaster NCE-CampusInsight: https://support.huawei.com/enterprise/en/network-management/imaster-nce-campusinsight-pid-15181085
350. Huawei Autonomous Driving Network MPLS: https://support.huawei.com/enterprise/en/network-management/adn-pid-15181086
351. Huawei MPLS White Paper: https://www.huawei.com/en/publications-and-communications/white-papers
352. Huawei IP Network MPLS: https://www.huawei.com/en/enterprise-networks/products/routers
353. Huawei Enterprise Support: https://support.huawei.com/enterprise/en/index.html
354. Huawei Community: https://forum.huawei.com/enterprise/en/index.html
355. Huawei Learning: https://e.huawei.com/en/certifications/
356. Huawei Developer: https://developer.huawei.com/consumer/en/
357. Huawei Cloud: https://www.huaweicloud.com/intl/en-us/
358. Huawei Research: https://www.huawei.com/en/research
359. Huawei Security: https://www.huawei.com/en/security
360. Huawei Open Source: https://www.huawei.com/en/open-source

### Nokia/Alcatel-Lucent Documentation

361. Nokia SR Linux MPLS: https://documentation.nokia.com/srlinux/22-6/html/t-intro/index.html
362. Nokia SR OS MPLS: https://documentation.nokia.com/sr/23-3/html/t-intro/index.html
363. Nokia 7750 SR MPLS: https://documentation.nokia.com/sr/23-3/books/mpls-services/index.html
364. Nokia 7450 ESS MPLS: https://documentation.nokia.com/sr/23-3/books/mpls-services/index.html
365. Nokia 7950 XRS MPLS: https://documentation.nokia.com/sr/23-3/books/mpls-services/index.html
366. Nokia VSR MPLS: https://documentation.nokia.com/sr/23-3/books/mpls-services/index.html
367. Nokia MPLS LDP: https://documentation.nokia.com/sr/23-3/books/ldp/index.html
368. Nokia MPLS RSVP-TE: https://documentation.nokia.com/sr/23-3/books/rsvp-te/index.html
369. Nokia MPLS Traffic Engineering: https://documentation.nokia.com/sr/23-3/books/mpls-traffic-engineering/index.html
370. Nokia MPLS VPN: https://documentation.nokia.com/sr/23-3/books/mpls-vpns/index.html
371. Nokia VPLS: https://documentation.nokia.com/sr/23-3/books/vpls/index.html
372. Nokia VPWS: https://documentation.nokia.com/sr/23-3/books/vpws/index.html
373. Nokia EVPN: https://documentation.nokia.com/sr/23-3/books/evpn/index.html
374. Nokia Segment Routing: https://documentation.nokia.com/sr/23-3/books/segment-routing/index.html
375. Nokia MPLS-TP: https://documentation.nokia.com/sr/23-3/books/mpls-tp/index.html
376. Nokia MPLS OAM: https://documentation.nokia.com/sr/23-3/books/mpls-oam/index.html
377. Nokia MPLS FRR: https://documentation.nokia.com/sr/23-3/books/mpls-frr/index.html
378. Nokia MPLS Multicast: https://documentation.nokia.com/sr/23-3/books/mpls-multicast/index.html
379. Nokia MPLS IPv6: https://documentation.nokia.com/sr/23-3/books/mpls-ipv6/index.html
380. Nokia MPLS Inter-AS: https://documentation.nokia.com/sr/23-3/books/mpls-inter-as/index.html
381. Nokia Network Services Platform MPLS: https://documentation.nokia.com/network-services-platform/index.html
382. Nokia NSP NFM-P: https://documentation.nokia.com/nsp/index.html
383. Nokia NSP SDN MPLS: https://documentation.nokia.com/nsp/index.html
384. Nokia WaveSuite MPLS: https://documentation.nokia.com/wavesuite/index.html
385. Nokia Altiplano MPLS: https://documentation.nokia.com/altiplano/index.html
386. Nokia DAC MPLS: https://documentation.nokia.com/dac/index.html
387. Nokia Support: https://www.nokia.com/networks/support/
388. Nokia Bell Labs: https://www.bell-labs.com/
389. Nokia Research: https://www.nokia.com/about-us/research/
390. Nokia Networks: https://www.nokia.com/networks/
391. Nokia Cloud and Network Services: https://www.nokia.com/networks/cloud-network-services/
392. Nokia IP Routing: https://www.nokia.com/networks/ip-routing/
393. Nokia Optical Networks: https://www.nokia.com/networks/optical-networks/
394. Nokia Fixed Networks: https://www.nokia.com/networks/fixed-networks/
395. Nokia Submarine Networks: https://www.nokia.com/networks/submarine-networks/
396. Nokia Campus Switching: https://www.nokia.com/networks/enterprise/campus-switching/
397. Nokia Data Center: https://www.nokia.com/networks/enterprise/data-center/
398. Nokia Industrial: https://www.nokia.com/networks/enterprise/industrial/
399. Nokia Transportation: https://www.nokia.com/networks/enterprise/transportation/
400. Nokia Public Safety: https://www.nokia.com/networks/enterprise/public-safety/

### Arista Documentation

401. Arista MPLS Overview: https://www.arista.com/en/um-eos/eos-mpls-overview
402. Arista MPLS Configuration: https://www.arista.com/en/um-eos/eos-mpls-configuration
403. Arista MPLS LDP: https://www.arista.com/en/um-eos/eos-mpls-ldp
404. Arista MPLS RSVP-TE: https://www.arista.com/en/um-eos/eos-mpls-rsvp-te
405. Arista MPLS Traffic Engineering: https://www.arista.com/en/um-eos/eos-mpls-traffic-engineering
406. Arista MPLS VPN: https://www.arista.com/en/um-eos/eos-mpls-vpn
407. Arista VPLS: https://www.arista.com/en/um-eos/eos-vpls
408. Arista EVPN MPLS: https://www.arista.com/en/um-eos/eos-evpn-mpls
409. Arista Segment Routing: https://www.arista.com/en/um-eos/eos-segment-routing
410. Arista MPLS-TP: https://www.arista.com/en/um-eos/eos-mpls-tp
411. Arista MPLS OAM: https://www.arista.com/en/um-eos/eos-mpls-oam
412. Arista MPLS FRR: https://www.arista.com/en/um-eos/eos-mpls-frr
413. Arista MPLS QoS: https://www.arista.com/en/um-eos/eos-mpls-qos
414. Arista MPLS Multicast: https://www.arista.com/en/um-eos/eos-mpls-multicast
415. Arista MPLS IPv6: https://www.arista.com/en/um-eos/eos-mpls-ipv6
416. Arista CloudVision: https://www.arista.com/en/products/eos/eos-cloudvision
417. Arista CloudVision Portal: https://www.arista.com/en/products/eos/eos-cloudvision-portal
418. Arista DANZ: https://www.arista.com/en/products/eos/eos-danz
419. Arista NetDB: https://www.arista.com/en/products/eos/eos-netdb
420. Arista TerminAttr: https://www.arista.com/en/products/eos/eos-terminattr
421. Arista AVD: https://avd.sh/
422. Arista ANTA: https://anta.ninja/
423. Arista CVP API: https://www.arista.com/en/support/toi/eos-4-26-0f/14874-cloudvision-portal-apis
424. Arista eAPI: https://www.arista.com/en/um-eos/eos-command-api
425. Arista SysDb: https://www.arista.com/en/um-eos/eos-system-database
426. Arista EOS Central: https://eos.arista.com/
427. Arista Community: https://www.arista.com/en/support/community
428. Arista Support: https://www.arista.com/en/support
429. Arista Training: https://www.arista.com/en/support/training
430. Arista Certification: https://www.arista.com/en/support/certification
431. Arista Research: https://www.arista.com/en/company/research
432. Arista Blog: https://www.arista.com/en/company/blog
433. Arista White Papers: https://www.arista.com/en/company/white-papers
434. Arista The Cloud Network: https://www.arista.com/en/solutions/cloud-networking
435. Arista Data Center: https://www.arista.com/en/solutions/data-center
436. Arista Campus: https://www.arista.com/en/solutions/campus
437. Arista DCI: https://www.arista.com/en/solutions/dci
438. Arista Service Provider: https://www.arista.com/en/solutions/service-provider
439. Arista Edge: https://www.arista.com/en/solutions/edge
440. Arista 7000 Series: https://www.arista.com/en/products/7000-series
441. Arista 7500 Series: https://www.arista.com/en/products/7500-series
442. Arista 7280R Series: https://www.arista.com/en/products/7280r-series
443. Arista 7800R Series: https://www.arista.com/en/products/7800r-series
444. Arista 7170 Series: https://www.arista.com/en/products/7170-series
445. Arista 7130 Series: https://www.arista.com/en/products/7130-series
446. Arista DCS-7300: https://www.arista.com/en/products/7300-series
447. Arista DCS-7060X: https://www.arista.com/en/products/7060x-series
448. Arista DCS-7020R: https://www.arista.com/en/products/7020r-series
449. Arista DCS-7010T: https://www.arista.com/en/products/7010t-series
450. Arista DCS-7050X: https://www.arista.com/en/products/7050x-series

### IETF Working Groups

451. MPLS Working Group: https://datatracker.ietf.org/wg/mpls/documents/
452. TEAS Working Group: https://datatracker.ietf.org/wg/teas/documents/
453. PCE Working Group: https://datatracker.ietf.org/wg/pce/documents/
454. SPRING Working Group: https://datatracker.ietf.org/wg/spring/documents/
455. BFD Working Group: https://datatracker.ietf.org/wg/bfd/documents/
456. CCAMP Working Group: https://datatracker.ietf.org/wg/ccamp/documents/
457. L3SM Working Group: https://datatracker.ietf.org/wg/l3sm/documents/
458. L2SM Working Group: https://datatracker.ietf.org/wg/l2sm/documents/
459. BESS Working Group: https://datatracker.ietf.org/wg/bess/documents/
460. BIER Working Group: https://datatracker.ietf.org/wg/bier/documents/
461. DETNET Working Group: https://datatracker.ietf.org/wg/detnet/documents/
462. IDR Working Group: https://datatracker.ietf.org/wg/idr/documents/
463. ISIS Working Group: https://datatracker.ietf.org/wg/isis/documents/
464. OSPF Working Group: https://datatracker.ietf.org/wg/ospf/documents/
465. RTGWG Working Group: https://datatracker.ietf.org/wg/rtgwg/documents/
466. GROW Working Group: https://datatracker.ietf.org/wg/grow/documents/
467. NANO Working Group: https://datatracker.ietf.org/wg/nano/documents/
468. SFC Working Group: https://datatracker.ietf.org/wg/sfc/documents/
469. LWIG Working Group: https://datatracker.ietf.org/wg/lwig/documents/
470. NETMOD Working Group: https://datatracker.ietf.org/wg/netmod/documents/
471. NETCONF Working Group: https://datatracker.ietf.org/wg/netconf/documents/
472. RESTCONF Working Group: https://datatracker.ietf.org/wg/restconf/documents/
473. ANIMA Working Group: https://datatracker.ietf.org/wg/anima/documents/
474. IPPM Working Group: https://datatracker.ietf.org/wg/ippm/documents/
475. NMRG Working Group: https://datatracker.ietf.org/rg/nmrg/documents/
476. PANRG Working Group: https://datatracker.ietf.org/rg/panrg/documents/
477. MAPRG Working Group: https://datatracker.ietf.org/rg/maprg/documents/
478. DINRG Working Group: https://datatracker.ietf.org/rg/dinrg/documents/
479. CFRG Working Group: https://datatracker.ietf.org/wg/cfrg/documents/
480. SAAG Working Group: https://datatracker.ietf.org/wg/saag/documents/
481. MPLS WG Charter: https://datatracker.ietf.org/wg/mpls/about/
482. MPLS WG Mailing List: https://mailarchive.ietf.org/arch/browse/mpls/
483. MPLS WG Meeting Materials: https://datatracker.ietf.org/meeting/materials/
484. MPLS WG Internet-Drafts: https://datatracker.ietf.org/wg/mpls/documents/
485. MPLS WG RFCs: https://datatracker.ietf.org/wg/mpls/documents/#rfcs
486. TEAS WG Charter: https://datatracker.ietf.org/wg/teas/about/
487. TEAS WG Mailing List: https://mailarchive.ietf.org/arch/browse/teas/
488. PCE WG Charter: https://datatracker.ietf.org/wg/pce/about/
489. PCE WG Mailing List: https://mailarchive.ietf.org/arch/browse/pce/
490. SPRING WG Charter: https://datatracker.ietf.org/wg/spring/about/
491. SPRING WG Mailing List: https://mailarchive.ietf.org/arch/browse/spring/
492. BFD WG Charter: https://datatracker.ietf.org/wg/bfd/about/
493. BFD WG Mailing List: https://mailarchive.ietf.org/arch/browse/bfd/
494. BESS WG Charter: https://datatracker.ietf.org/wg/bess/about/
495. BESS WG Mailing List: https://mailarchive.ietf.org/arch/browse/bess/
496. BIER WG Charter: https://datatracker.ietf.org/wg/bier/about/
497. BIER WG Mailing List: https://mailarchive.ietf.org/arch/browse/bier/
498. CCAMP WG Charter: https://datatracker.ietf.org/wg/ccamp/about/
499. CCAMP WG Mailing List: https://mailarchive.ietf.org/arch/browse/ccamp/
500. IDR WG Mailing List: https://mailarchive.ietf.org/arch/browse/idr/

### Packet Analysis Tools

501. Wireshark MPLS filters: https://wiki.wireshark.org/MPLS
502. Wireshark LDP filters: https://wiki.wireshark.org/LDP
503. Wireshark RSVP filters: https://wiki.wireshark.org/RSVP
504. Wireshark BGP filters: https://wiki.wireshark.org/BGP
505. Wireshark BFD filters: https://wiki.wireshark.org/BFD
506. Wireshark PW filters: https://wiki.wireshark.org/PW
507. Wireshark VXLAN filters: https://wiki.wireshark.org/VXLAN
508. Wireshark ERSPAN filters: https://wiki.wireshark.org/ERSPAN
509. Wireshark Capture Filters: https://wiki.wireshark.org/CaptureFilters
510. Wireshark Display Filters: https://wiki.wireshark.org/DisplayFilters
511. tcpdump MPLS: https://www.tcpdump.org/manpages/tcpdump.1.html
512. tshark MPLS: https://www.wireshark.org/docs/man-pages/tshark.html
513. Scapy MPLS: https://scapy.readthedocs.io/en/latest/api/scapy.layers.html
514. Scapy docs: https://scapy.readthedocs.io/
515. PyShark: https://github.com/KimiNewt/pyshark
516. libpcap: https://www.tcpdump.org/
517. WinPcap: https://www.winpcap.org/
518. Npcap: https://nmap.org/npcap/
519. USBPcap: https://desowin.org/usbpcap/
520. CloudShark: https://www.cloudshark.org/
521. PacketTotal: https://www.packettotal.com/
522. NetworkMiner: https://www.netresec.com/?page=NetworkMiner
523. CapLoader: https://www.netresec.com/?page=CapLoader
524. Packet Sender: https://packetsender.com/
525. Ostinato: https://ostinato.org/
526. TRex: https://trex-tgn.cisco.com/
527. Iperf: https://iperf.fr/
528. Iperf3: https://github.com/esnet/iperf
529. MTR: https://github.com/traviscross/mtr
530. hping3: http://www.hping.org/
531. nping: https://nmap.org/nping/
532. ping: https://en.wikipedia.org/wiki/Ping_(networking_utility)
533. traceroute: https://en.wikipedia.org/wiki/Traceroute
534. tracepath: https://linux.die.net/man/8/tracepath
535. pathping: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/pathping
536. tcpreplay: https://tcpreplay.appneta.com/
537. pcapplusplus: https://pcapplusplus.github.io/
538. gopacket: https://github.com/google/gopacket
539. Pcap4J: https://www.pcap4j.org/
540. rust-pcap: https://github.com/rust-pcap/pcap
541. libtins: https://libtins.github.io/
542. Pcap.Net: https://pcapdotnet.codeplex.com/
543. jNetPcap: https://jnetpcap.com/
544. SharpPcap: https://github.com/dotpcap/sharppcap
545. Pypacker: https://github.com/mike01/pypacker
546. Kamene: https://github.com/phaethon/kamene
547. impacket: https://github.com/fortra/impacket
548. pysap: https://github.com/SecureAuthCorp/pysap
549. dpkt: https://github.com/kbandla/dpkt
550. construct: https://construct.readthedocs.io/
551. Kaitai Struct: https://kaitai.io/
552. Binwalk: https://github.com/ReFirmLabs/binwalk
553. Netcat: https://en.wikipedia.org/wiki/Netcat
554. Socat: http://www.dest-unreach.org/socat/
555. Nmap: https://nmap.org/
556. ZMap: https://zmap.io/
557. Masscan: https://github.com/robertdavidgraham/masscan
558. P0f: https://lcamtuf.coredump.cx/p0f3/
559. Zeek: https://zeek.org/
560. Suricata: https://suricata.io/
561. Snort: https://www.snort.org/
562. Moloch: https://arkime.com/
563. Security Onion: https://securityonion.net/
564. Wazuh: https://wazuh.com/
565. ELK Stack: https://www.elastic.co/elastic-stack
566. Splunk: https://www.splunk.com/
567. Grafana: https://grafana.com/
568. Prometheus: https://prometheus.io/
569. InfluxDB: https://www.influxdata.com/
570. Telegraf: https://www.influxdata.com/time-series-platform/telegraf/
571. Cacti: https://www.cacti.net/
572. Nagios: https://www.nagios.org/
573. Zabbix: https://www.zabbix.com/
574. PRTG: https://www.paessler.com/prtg
575. LibreNMS: https://www.librenms.org/
576. Observium: https://www.observium.org/
577. NetBox: https://netbox.dev/
578. Nautobot: https://www.nautobot.com/
579. phpIPAM: https://phpipam.net/
580. RackTables: https://racktables.org/
581. Oxidized: https://github.com/ytti/oxidized
582. RANCID: https://www.shrubbery.net/rancid/
583. Batfish: https://www.batfish.org/
584. Netomator: https://github.com/NetworkAutomationForum/
585. Ansible: https://www.ansible.com/
586. Netmiko: https://github.com/ktbyers/netmiko
587. NAPALM: https://github.com/napalm-automation/napalm
588. Nornir: https://nornir.readthedocs.io/
589. SaltStack: https://saltproject.io/
590. Puppet: https://www.puppet.com/
590. Chef: https://www.chef.io/
591. Terraform: https://www.terraform.io/
592. Pulumi: https://www.pulumi.com/
593. pyATS: https://developer.cisco.com/pyats/
594. Genie: https://developer.cisco.com/docs/genie-docs/
595. Scrapli: https://github.com/carlmontanari/scrapli
596. Paramiko: https://www.paramiko.org/
597. Exscript: https://github.com/knipknap/exscript
598. Fabric: https://www.fabfile.org/
599. Invoke: https://www.pyinvoke.org/
600. Click: https://click.palletsprojects.com/

### Programming & Simulation

601. Python: https://www.python.org/
602. Python Tkinter docs: https://docs.python.org/3/library/tkinter.html
603. Python Canvas: https://docs.python.org/3/library/tkinter.html#canvas
604. Matplotlib: https://matplotlib.org/
605. NumPy: https://numpy.org/
606. NetworkX: https://networkx.org/
607. Graphviz: https://graphviz.org/
608. PyGraphviz: https://pygraphviz.github.io/
609. pydot: https://github.com/pydot/pydot
610. Pillow: https://python-pillow.org/
611. Pygame: https://www.pygame.org/
612. PyOpenGL: http://pyopengl.sourceforge.net/
613. ModernGL: https://moderngl.readthedocs.io/
614. Panda3D: https://www.panda3d.org/
615. Ursina Engine: https://www.ursinaengine.org/
616. Blender Python API: https://docs.blender.org/api/current/
617. MayaVi: https://docs.enthought.com/mayavi/mayavi/
618. Plotly: https://plotly.com/python/
619. Bokeh: https://bokeh.org/
620. Dash: https://dash.plotly.com/
621. Streamlit: https://streamlit.io/
622. Gradio: https://gradio.app/
623. PyQt: https://riverbankcomputing.com/software/pyqt/
624. PySide: https://wiki.qt.io/Qt_for_Python
625. Kivy: https://kivy.org/
626. Dear PyGui: https://github.com/hoffstadt/DearPyGui
627. Eel: https://github.com/python-eel/Eel
628. Flask: https://flask.palletsprojects.com/
629. FastAPI: https://fastapi.tiangolo.com/
630. Django: https://www.djangoproject.com/
631. Tornado: https://www.tornadoweb.org/
632. aiohttp: https://docs.aiohttp.org/
633. Twisted: https://twistedmatrix.com/
634. ZeroMQ: https://zeromq.org/
635. RabbitMQ: https://www.rabbitmq.com/
636. Redis: https://redis.io/
637. SQLite: https://www.sqlite.org/
638. PostgreSQL: https://www.postgresql.org/
639. MySQL: https://www.mysql.com/
640. MongoDB: https://www.mongodb.com/
641. SQLAlchemy: https://www.sqlalchemy.org/
642. Peewee: http://docs.peewee-orm.com/
643. Pony ORM: https://ponyorm.org/
644. Tortoise ORM: https://tortoise-orm.readthedocs.io/
645. Pydantic: https://docs.pydantic.dev/
646. Celery: https://docs.celeryq.dev/
647. Dramatiq: https://dramatiq.io/
648. APScheduler: https://apscheduler.readthedocs.io/
649. schedule: https://schedule.readthedocs.io/
650. watchdog: https://python-watchdog.readthedocs.io/
651. Loguru: https://loguru.readthedocs.io/
652. Rich: https://rich.readthedocs.io/
653. Typer: https://typer.tiangolo.com/
654. Argparse: https://docs.python.org/3/library/argparse.html
655. ConfigParser: https://docs.python.org/3/library/configparser.html
656. JSON: https://docs.python.org/3/library/json.html
657. YAML: https://pyyaml.org/
658. TOML: https://toml.io/
659. CSV: https://docs.python.org/3/library/csv.html
660. Pickle: https://docs.python.org/3/library/pickle.html
661. Shelve: https://docs.python.org/3/library/shelve.html
662. DBM: https://docs.python.org/3/library/dbm.html
663. SQLite3: https://docs.python.org/3/library/sqlite3.html
664. Asyncio: https://docs.python.org/3/library/asyncio.html
665. Threading: https://docs.python.org/3/library/threading.html
666. Multiprocessing: https://docs.python.org/3/library/multiprocessing.html
667. Queue: https://docs.python.org/3/library/queue.html
668. Socket: https://docs.python.org/3/library/socket.html
669. Select: https://docs.python.org/3/library/select.html
670. Subprocess: https://docs.python.org/3/library/subprocess.html
671. OS: https://docs.python.org/3/library/os.html
672. Sys: https://docs.python.org/3/library/sys.html
673. Pathlib: https://docs.python.org/3/library/pathlib.html
674. Shutil: https://docs.python.org/3/library/shutil.html
675. Glob: https://docs.python.org/3/library/glob.html
676. Re: https://docs.python.org/3/library/re.html
677. Itertools: https://docs.python.org/3/library/itertools.html
678. Collections: https://docs.python.org/3/library/collections.html
679. Dataclasses: https://docs.python.org/3/library/dataclasses.html
680. Enum: https://docs.python.org/3/library/enum.html
681. Typing: https://docs.python.org/3/library/typing.html
682. Hashlib: https://docs.python.org/3/library/hashlib.html
683. Secrets: https://docs.python.org/3/library/secrets.html
684. Random: https://docs.python.org/3/library/random.html
685. Math: https://docs.python.org/3/library/math.html
686. Statistics: https://docs.python.org/3/library/statistics.html
687. Decimal: https://docs.python.org/3/library/decimal.html
688. Fractions: https://docs.python.org/3/library/fractions.html
689. Time: https://docs.python.org/3/library/time.html
690. Datetime: https://docs.python.org/3/library/datetime.html
691. Calendar: https://docs.python.org/3/library/calendar.html
692. Zoneinfo: https://docs.python.org/3/library/zoneinfo.html
693. Timeit: https://docs.python.org/3/library/timeit.html
694. Profile: https://docs.python.org/3/library/profile.html
695. CProfile: https://docs.python.org/3/library/profile.html
696. Trace: https://docs.python.org/3/library/trace.html
697. Doctest: https://docs.python.org/3/library/doctest.html
698. Unittest: https://docs.python.org/3/library/unittest.html
699. Pytest: https://docs.pytest.org/
700. Hypothesis: https://hypothesis.readthedocs.io/

### Books

701. "MPLS Fundamentals" by Luc De Ghein
702. "MPLS-Enabled Applications" by Ina Minei and Julian Lucek
703. "MPLS in the SDN Era" by Antonio Sanchez-Mongallon, Daniel Voyer, et al.
704. "Definitive MPLS Network Designs" by Jim Guichard, François Le Faucheur, Jean-Philippe Vasseur
705. "BGP/MPLS IP VPNs" by Joshua G. S. (various)
706. "Traffic Engineering with MPLS" by Eric Osborne and Ajay Simha
707. "MPLS Configuration on Cisco IOS Software" by Lancy Lobo and Umesh Lakshman
708. "Juniper MX Series" by Douglas Richard Hanks Jr., Harry Reynolds, David Roy
709. "Juniper SRX Series" by Brad Woodberg and Rob Cameron
710. "Cisco IOS XR Fundamentals" by Mobeen Tahir, Mark Ghattas, Dawit Birhanu
711. "Cisco Carrier Routing Architectures" by Ahmed Afrose, Mohan Guruswamy
712. "Network Warrior" by Gary A. Donahue
713. "Routing TCP/IP, Volume I" by Jeff Doyle
714. "Routing TCP/IP, Volume II" by Jeff Doyle
715. "CCIE Routing and Switching v5.0" by Narbik Kocharians
716. "CCIE Service Provider v4.1" by Nicolas Michel
717. "Network Programmability and Automation" by Jason Edelman, Scott S. Lowe, Matt Oswalt
718. "Automating the SDN Data Center" by Vivek Tiwari
719. "Software-Defined Networking: A Systems Approach" by Larry Peterson and Carmelo Cascone
720. "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross
721. "TCP/IP Illustrated, Volume 1" by Kevin R. Fall and Richard W. Stevens
722. "TCP/IP Illustrated, Volume 2" by Gary R. Wright and W. Richard Stevens
723. "TCP/IP Illustrated, Volume 3" by W. Richard Stevens
724. "Internetworking with TCP/IP Vol.1" by Douglas E. Comer
725. "The TCP/IP Guide" by Charles M. Kozierok
726. "Packet Guide to Routing and Switching" by Bruce Hartpence
727. "Packet Guide to Core Network Protocols" by Bruce Hartpence
728. "Packet Guide to Voice over IP" by Bruce Hartpence
729. "Practical Packet Analysis" by Chris Sanders
730. "Wireshark Network Analysis" by Laura Chappell and Gerald Combs
731. "Network Flow Analysis" by Michael W. Lucas
732. "Absolute FreeBSD" by Michael W. Lucas
733. "Linux Networking Cookbook" by Carla Schroder
734. "UNIX and Linux System Administration Handbook" by Evi Nemeth et al.
735. "The Practice of System and Network Administration" by Thomas A. Limoncelli et al.
736. "Site Reliability Engineering" by Google
737. "The Site Reliability Workbook" by Google
738. "Building Secure Networks" by Steven Brown
739. "Network Security Assessment" by Chris McNab
740. "Metasploit: The Penetration Tester's Guide" by David Kennedy et al.
741. "The Hacker Playbook" by Peter Kim
742. "Hacking: The Art of Exploitation" by Jon Erickson
743. "Black Hat Python" by Justin Seitz
744. "Gray Hat Python" by Justin Seitz
745. "Violent Python" by TJ O'Connor
746. "Penetration Testing" by Georgia Weidman
747. "The Web Application Hacker's Handbook" by Dafydd Stuttard
748. "Real-World Bug Hunting" by Peter Yaworski
749. "Bug Bounty Bootcamp" by Vickie Li
750. "Hands-On Ethical Hacking and Network Defense" by Michael T. Simpson

### Online Courses & Training

751. Cisco Networking Academy: https://www.netacad.com/
752. Juniper Open Learning: https://www.juniper.net/us/en/training/open-learning.html
753. Huawei ICT Academy: https://e.huawei.com/en/talent/ict-academy/
754. Arista Training: https://www.arista.com/en/support/training
755. Nokia Learning Services: https://www.nokia.com/networks/training/
756. Coursera Computer Networking: https://www.coursera.org/specializations/computer-communications
757. Coursera Network Security: https://www.coursera.org/specializations/network-security
758. edX Computer Networks: https://www.edx.org/learn/computer-networking
759. Udemy Networking Courses: https://www.udemy.com/topic/networking/
760. Pluralsight Networking: https://www.pluralsight.com/paths/networking
761. LinkedIn Learning Networking: https://www.linkedin.com/learning/topics/networking
762. INE Networking: https://ine.com/learning/paths
763. CBT Nuggets Networking: https://www.cbtnuggets.com/it-training/networking
764. ITProTV Networking: https://www.itpro.tv/courses/networking/
765. Network Chuck YouTube: https://www.youtube.com/c/NetworkChuck
766. David Bombal YouTube: https://www.youtube.com/c/DavidBombal
767. Jeremy's IT Lab: https://www.youtube.com/c/JeremysITLab
768. Keith Barker YouTube: https://www.youtube.com/c/KeithBarker
769. Practicum by Orhan Ergun: https://www.orhanergun.net/
770. IPSpace.net: https://www.ipspace.net/
771. Packet Pushers: https://packetpushers.net/
772. Network Collective: https://thenetworkcollective.com/
773. Heavy Networking Podcast: https://packetpushers.net/series/heavy-networking/
774. Day Two Cloud: https://packetpushers.net/series/day-two-cloud/
775. Kubernetes Unpacked: https://packetpushers.net/series/kubernetes-unpacked/
776. Tech Bytes: https://packetpushers.net/series/tech-bytes/
777. The Network Break: https://packetpushers.net/series/the-network-break/
778. Bufferbloat Project: https://www.bufferbloat.net/
779. NANOG: https://www.nanog.org/
780. RIPE NCC: https://www.ripe.net/
781. APNIC: https://www.apnic.net/
782. ARIN: https://www.arin.net/
783. LACNIC: https://www.lacnic.net/
784. AFRINIC: https://www.afrinic.net/
785. Internet Society: https://www.internetsociety.org/
786. IETF Education: https://www.ietf.org/education/
787. Internet Hall of Fame: https://www.internethalloffame.org/
788. World Wide Web Consortium: https://www.w3.org/
789. ICANN: https://www.icann.org/
790. ISOC Chad: https://www.internetsociety.org/chapter/tchad/
791. Africacom: https://www.africacom.com/
792. Africa Tech Festival: https://www.africatechfestival.com/
793. GitHub Learning Lab: https://lab.github.com/
794. GitLab Learn: https://about.gitlab.com/learn/
795. Microsoft Learn Networking: https://docs.microsoft.com/en-us/learn/networking/
796. AWS Networking Training: https://aws.amazon.com/training/networking/
797. Azure Networking Training: https://docs.microsoft.com/en-us/learn/azure/
798. GCP Networking Training: https://cloud.google.com/training
799. OCI Networking Training: https://education.oracle.com/
800. IBM Cloud Networking: https://www.ibm.com/cloud/learn/networking

### Labs & Sandboxes

801. Cisco DevNet Sandbox: https://developer.cisco.com/site/sandbox/
802. Cisco Modeling Labs: https://developer.cisco.com/modeling-labs/
803. Cisco VIRL: https://developer.cisco.com/docs/virl/
804. GNS3: https://www.gns3.com/
805. EVE-NG: https://www.eve-ng.net/
806. Packet Tracer: https://www.netacad.com/courses/packet-tracer
807. UNL: https://www.unetlab.com/
808. Containerlab: https://containerlab.dev/
809. Kathará: https://www.kathara.org/
810. Mininet: http://mininet.org/
811. CORE: https://github.com/coreemu/core
812. IMUNES: https://imunes.net/
813. Netkit: https://wiki.netkit.org/
814. VNX: http://www.dit.upm.es/vnx/
815. Marionnet: http://www.marionnet.org/
816. Psimulator2: https://github.com/danielkappelle/psimulator2
817. Dynamips: https://github.com/GNS3/dynamips
818. IOU: https://github.com/your/iou
819. vIOS: https://developer.cisco.com/docs/virl/
820. vIOS-L2: https://developer.cisco.com/docs/virl/
821. vSRX: https://www.juniper.net/us/en/dm/free-vsrx-trial.html
822. vMX: https://www.juniper.net/us/en/dm/free-vmx-trial.html
823. vPTX: https://www.juniper.net/us/en/dm/free-vptx-trial.html
824. vQFX: https://www.juniper.net/us/en/dm/free-vqfx-trial.html
825. cRPD: https://www.juniper.net/us/en/dm/free-crpd-trial.html
826. vEOS: https://www.arista.com/en/products/software/vEOS
827. cEOS: https://www.arista.com/en/products/software/containerized-eos
828. Nokia SR Linux: https://www.nokia.com/networks/products/service-router-linux/
829. Nokia SR OS: https://www.nokia.com/networks/products/7750-service-router/
830. FRRouting: https://frrouting.org/
831. BIRD: https://bird.network.cz/
832. Quagga: https://www.nongnu.org/quagga/
833. GoBGP: https://osrg.github.io/gobgp/
834. ExaBGP: https://github.com/Exa-Networks/exabgp
835. MPLS Linux Kernel: https://www.kernel.org/doc/html/latest/networking/mpls-sysctl.html
836. Linux MPLS HowTo: https://docs.cumulusnetworks.com/
837. Cumulus Linux MPLS: https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-50/Layer-3/Multiprotocol-Label-Switching-MPLS/
838. VyOS MPLS: https://docs.vyos.io/en/latest/configuration/mpls/index.html
839. TNSR MPLS: https://www.netgate.com/products/tnsr.html
840. pfSense: https://www.pfsense.org/
841. OPNsense: https://opnsense.org/
842. OpenWrt: https://openwrt.org/
843. DD-WRT: https://dd-wrt.com/
844. MikroTik RouterOS: https://help.mikrotik.com/
845. MikroTik MPLS: https://wiki.mikrotik.com/wiki/Manual:MPLSVPLS
846. Ubiquiti EdgeRouter: https://help.ui.com/hc/en-us
847. Fortinet MPLS: https://docs.fortinet.com/
848. Palo Alto Networks: https://docs.paloaltonetworks.com/
849. Check Point: https://sc1.checkpoint.com/documents/
850. Sophos: https://docs.sophos.com/

### Security & Hacking

851. OWASP: https://owasp.org/
852. NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
853. MITRE ATT&CK: https://attack.mitre.org/
854. MITRE D3FEND: https://d3fend.mitre.org/
855. CVE Database: https://cve.mitre.org/
856. NVD: https://nvd.nist.gov/
857. Exploit-DB: https://www.exploit-db.com/
858. Metasploit: https://www.metasploit.com/
859. Kali Linux: https://www.kali.org/
860. Parrot OS: https://www.parrotsec.org/
861. BlackArch: https://blackarch.org/
862. Pentoo: https://www.pentoo.ch/
863. BackBox: https://www.backbox.org/
864. DEF CON: https://www.defcon.org/
865. Black Hat: https://www.blackhat.com/
866. RSA Conference: https://www.rsaconference.com/
867. BSides: https://www.securitybsides.com/
868. Nullcon: https://nullcon.net/
869. HITB: https://conference.hitb.org/
870. 44CON: https://44con.com/
871. HackFest: https://hackfest.ca/
872. SteelCon: https://www.steelcon.info/
873. GreHack: https://grehack.fr/
874. LeHack: https://lehack.org/
875. MCH2022: https://mch2022.org/
876. CCC: https://www.ccc.de/
877. Chaos Computer Club: https://www.ccc.de/
878. Hackaday: https://hackaday.com/
879. Hackster.io: https://www.hackster.io/
880. Instructables: https://www.instructables.com/
881. Replit: https://replit.com/
882. CodePen: https://codepen.io/
883. JSFiddle: https://jsfiddle.net/
884. TryHackMe: https://tryhackme.com/
885. Hack The Box: https://www.hackthebox.com/
886. VulnHub: https://www.vulnhub.com/
887. PentesterLab: https://pentesterlab.com/
888. PortSwigger Web Security Academy: https://portswigger.net/web-security
889. HackThisSite: https://www.hackthissite.org/
890. Root Me: https://www.root-me.org/
891. OverTheWire: https://overthewire.org/
892. picoCTF: https://picoctf.org/
893. CTFtime: https://ctftime.org/
894. CyberTalents: https://cybertalents.com/
895. CyberDiscovery: https://cyberdisc.io/
896. National Cyber Scholarship: https://www.nationalcyberscholarship.org/
897. SANS Cyber Aces: https://www.sans.org/cyberaces/
898. SANS NetWars: https://www.sans.org/netwars/
899. SANS SEC504: https://www.sans.org/cyber-security-courses/hacker-tools-techniques-exploits-incident-handling/
900. SANS SEC560: https://www.sans.org/cyber-security-courses/network-penetration-testing-ethical-hacking/

### African & Chadian Tech Communities

901. Hackers_Tchad: https://www.hackers-tchad.org/ (community placeholder)
902. Google Developer Groups N'Djamena: https://gdg.community.dev/
903. Facebook Developer Circles N'Djamena: https://developers.facebook.com/
904. Andela: https://www.andela.com/
905. ALX Africa: https://www.alxafrica.com/
906. African Leadership University: https://www.alueducation.com/
907. African Institute for Mathematical Sciences: https://nexteinstein.org/
808. Copicentre Tchad: https://copicentre-tchad.org/
909. Internet Society Chad: https://www.internetsociety.org/chapter/tchad/
910. AFRINIC: https://www.afrinic.net/
911. AfNOG: https://www.afnog.org/
912. AfPIF: https://www.afpif.org/
913. AXIS: https://www.internetsociety.org/axis/
914. Network Startup Resource Center: https://nsrc.org/
915. ISOC African Chapters: https://www.internetsociety.org/chapters/
916. TechCabal: https://techcabal.com/
917. Disrupt Africa: https://disrupt-africa.com/
918. Ventureburn: https://ventureburn.com/
919. WeeTracker: https://weetracker.com/
920. How we made it in Africa: https://www.howwemadeitinafrica.com/
921. African Tech Roundup: https://africantechroundup.com/
922. The Nerve Africa: https://thenerveafrica.com/
923. Techpoint Africa: https://techpoint.africa/
924. PesaCheck: https://pesacheck.org/
925. Code for Africa: https://codeforafrica.org/
926. African Digital Rights Network: https://adrcollective.org/
927. Paradigm Initiative: https://paradigmhq.org/
928. CIPESA: https://cipesa.org/
929. Access Now: https://www.accessnow.org/
930. Committee to Protect Journalists Africa: https://cpj.org/africa/
931. Internet Freedom Festival: https://internetfreedomfestival.org/
932. RightsCon: https://www.rightscon.org/
933. FIFAfrica: https://fifafrica.net/
934. Africa Internet Summit: https://afrinic.net/afrinis
935. AfricaCom: https://www.africacom.com/
936. AfricaTech: https://www.africatechfestival.com/
937. GITEX Africa: https://gitexafrica.com/
938. VivaTech Africa: https://vivatechnology.com/
939. Startupbootcamp AfriTech: https://www.startupbootcamp.org/accelerator/afritech/
940. MEST Africa: https://mestafrica.com/
941. CcHUB: https://cchub.africa/
942. iHub Nairobi: https://ihub.co.ke/
943. BongoHive: https://bongohive.co.zm/
944. Kumasi Hive: https://kumasihive.com/
945. IceAddis: https://iceaddis.com/
946. Impact Hub: https://impacthub.net/
947. Nairobi Garage: https://nairobigarage.com/
948. The Baobab Network: https://www.baobabnetwork.com/
949. Flat6Labs: https://flat6labs.com/
950. Launch Africa Ventures: https://launchafricaventures.com/

### General Networking Resources

951. NetworkLessons.com: https://networklessons.com/
952. PacketLife.net: https://packetlife.net/
953. Routing-Bits.com: https://routing-bits.com/
954. NIL Learning: https://www.nil.com/
955. Fast Lane: https://www.fastlaneus.com/
956. Global Knowledge: https://www.globalknowledge.com/
957. New Horizons: https://www.newhorizons.com/
958. Learning Tree: https://www.learningtree.com/
959. TechSmith: https://www.techsmith.com/
960. SolarWinds: https://www.solarwinds.com/
961. ManageEngine: https://www.manageengine.com/
962. Lansweeper: https://www.lansweeper.com/
963. PDQ: https://www.pdq.com/
964. NirSoft: https://www.nirsoft.net/
965. Sysinternals: https://docs.microsoft.com/en-us/sysinternals/
966. Wireshark Certified Network Analyst: https://www.wcna.org/
967. CWNP: https://www.cwnp.com/
968. CompTIA Network+: https://www.comptia.org/certifications/network
969. CompTIA Security+: https://www.comptia.org/certifications/security
970. CompTIA CySA+: https://www.comptia.org/certifications/cybersecurity-analyst
971. CompTIA CASP+: https://www.comptia.org/certifications/comptia-advanced-security-practitioner
972. CompTIA PenTest+: https://www.comptia.org/certifications/pentest
973. EC-Council CEH: https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/
974. EC-Council LPT: https://www.eccouncil.org/programs/licensed-penetration-tester-lpt-master/
975. Offensive Security OSCP: https://www.offensive-security.com/pwk-oscp/
976. Offensive Security OSCE: https://www.offensive-security.com/awe-osce/
977. Offensive Security OSEP: https://www.offensive-security.com/osep/
978. Offensive Security OSWE: https://www.offensive-security.com/oswe/
979. Offensive Security OSED: https://www.offensive-security.com/osed/
980. Offensive Security OSEE: https://www.offensive-security.com/osee/
981. SANS GCIH: https://www.giac.org/certification/certified-incident-handler-gcih
982. SANS GPEN: https://www.giac.org/certification/penetration-tester-gpen
983. SANS GWAPT: https://www.giac.org/certification/web-application-penetration-tester-gwapt
984. SANS GXPN: https://www.giac.org/certification/exploit-researcher-advanced-penetration-tester-gxpn
985. SANS GSE: https://www.giac.org/certifications/global-information-assurance-certification-security-expert-gse/
986. ISACA CISM: https://www.isaca.org/credentialing/cism
987. ISACA CISA: https://www.isaca.org/credentialing/cisa
988. ISACA CRISC: https://www.isaca.org/credentialing/crisc
989. ISACA CGEIT: https://www.isaca.org/credentialing/cgeit
990. ISC2 CISSP: https://www.isc2.org/Certifications/CISSP
991. ISC2 CCSP: https://www.isc2.org/Certifications/CCSP
992. ISC2 SSCP: https://www.isc2.org/Certifications/SSCP
993. PMI PMP: https://www.pmi.org/certifications/project-management-pmp
994. ITIL Foundation: https://www.axelos.com/certifications/itil-service-management
995. TOGAF: https://www.opengroup.org/togaf
996. COBIT: https://www.isaca.org/resources/cobit
997. NIST SP 800-53: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
998. NIST SP 800-171: https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final
999. ISO/IEC 27001: https://www.iso.org/standard/27001
1000. ISO/IEC 27002: https://www.iso.org/standard/27002

### Additional Resources (1001-1100)

1001. RIPE Routing Working Group: https://www.ripe.net/participate/ripe/wg/routing-wg
1002. RIPE Database: https://apps.db.ripe.net/db-web-ui/
1003. RIPE Atlas: https://atlas.ripe.net/
1004. RIPEstat: https://stat.ripe.net/
1005. APNIC Training: https://www.apnic.net/community/training/
1006. APNIC Labs: https://labs.apnic.net/
1007. ARIN Routing: https://www.arin.net/resources/routing/
1008. LACNIC Training: https://www.lacnic.net/686/1/lacnic/training
1009. AFRINIC Training: https://www.afrinic.net/training
1010. Interconnection Survey: https://www.internetsociety.org/resources/depository/
1011. BGPStream: https://bgpstream.caida.org/
1012. CAIDA: https://www.caida.org/
1013. RouteViews: https://www.routeviews.org/
1014. RIPE RIS: https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris
1015. Packet Clearing House: https://www.pch.net/
1016. Team Cymru IP to ASN: https://www.team-cymru.com/IP-ASN-mapping.html
1017. Hurricane Electric BGP: https://bgp.he.net/
1018. NLNOG Ring: https://ring.nlnog.net/
1019. PeeringDB: https://www.peeringdb.com/
1020. Internet Exchange Database: https://www.euro-ix.net/
1021. DE-CIX: https://www.de-cix.net/
1022. AMS-IX: https://www.ams-ix.net/
1023. LINX: https://www.linx.net/
1024. Equinix Internet Exchange: https://ix.equinix.com/
1025. France-IX: https://www.france-ix.net/
1026. SwissIX: https://www.swissix.ch/
1027. Netnod: https://www.netnod.se/
1028. SIX: https://www.six.sk/
1029. BCIX: https://www.bcix.de/
1030. ECIX: https://www.ecix.net/
1031. INEX: https://www.inex.ie/
1032. LONAP: https://www.lonap.net/
1033. MAE-West: https://en.wikipedia.org/wiki/MAE-West
1034. MAE-East: https://en.wikipedia.org/wiki/MAE-East
1035. Cogent: https://www.cogentco.com/
1036. Level3: https://www.lumen.com/
1037. NTT Communications: https://www.ntt.com/
1038. Telia Carrier: https://www.teliacompany.com/
1039. GTT: https://www.gtt.net/
1040. Zayo: https://www.zayo.com/
1041. PCCW Global: https://www.pccwglobal.com/
1042. Orange: https://www.orange.com/
1043. Vodafone: https://www.vodafone.com/
1044. Telecom Italia Sparkle: https://www.tisparkle.com/
1045. Deutsche Telekom ICSS: https://www.telekom.com/
1046. BT: https://www.bt.com/
1047. AT&T: https://www.att.com/
1048. Verizon: https://www.verizon.com/
1049. Comcast: https://www.comcast.com/
1050. Charter: https://www.charter.com/
1051. Cox: https://www.cox.com/
1052. Altice: https://www.alticeusa.com/
1053. Frontier: https://frontier.com/
1054. Windstream: https://www.windstream.com/
1055. CenturyLink: https://www.lumen.com/
1056. Mediacom: https://www.mediacomcable.com/
1057. RCN: https://www.rcn.com/
1058. Sonic: https://www.sonic.com/
1059. Google Fiber: https://fiber.google.com/
1060. Starlink: https://www.starlink.com/
1061. OneWeb: https://oneweb.net/
1062. Amazon Kuiper: https://www.aboutamazon.com/what-we-do/devices-services/project-kuiper
1063. Telesat Lightspeed: https://www.telesat.com/
1064. Iridium: https://www.iridium.com/
1065. Inmarsat: https://www.inmarsat.com/
1066. SES: https://www.ses.com/
1067. Intelsat: https://www.intelsat.com/
1068. Eutelsat: https://www.eutelsat.com/
1069. Viasat: https://www.viasat.com/
1070. HughesNet: https://www.hughesnet.com/
1071. Ookla Speedtest: https://www.speedtest.net/
1072. Fast.com: https://fast.com/
1073. Measurement Lab: https://www.measurementlab.net/
1074. RIPE Atlas API: https://atlas.ripe.net/docs/api/
1075. PingPE: https://ping.pe/
1076. Looking Glass: https://looking.house/
1077. BGP Tools: https://bgp.tools/
1078. IPinfo: https://ipinfo.io/
1079. IP-API: https://ip-api.com/
1080. MaxMind GeoIP: https://www.maxmind.com/
1081. IP2Location: https://www.ip2location.com/
1082. DB-IP: https://db-ip.com/
1083. IPGeolocation: https://ipgeolocation.io/
1084. ipregistry: https://ipregistry.co/
1085. Abstract API: https://www.abstractapi.com/
1086. ipdata: https://ipdata.co/
1087. ipstack: https://ipstack.com/
1088. ipapi: https://ipapi.com/
1089. ipwhois: https://ipwhois.io/
1090. ip-api docs: https://ip-api.com/docs/
1091. whois: https://en.wikipedia.org/wiki/Whois
1092. RDAP: https://rdap.org/
1093. IANA Protocol Numbers: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
1094. IANA MPLS Label Values: https://www.iana.org/assignments/mpls-label-values/mpls-label-values.xhtml
1095. IANA MPLS Special-Purpose Label Values: https://www.iana.org/assignments/mpls-special-purpose-label-values/mpls-special-purpose-label-values.xhtml
1096. IANA RSVP Parameters: https://www.iana.org/assignments/rsvp-parameters/rsvp-parameters.xhtml
1097. IANA LDP Parameters: https://www.iana.org/assignments/ldp-namespaces/ldp-namespaces.xhtml
1098. IANA BGP Parameters: https://www.iana.org/assignments/bgp-parameters/bgp-parameters.xhtml
1099. IANA Address Family Numbers: https://www.iana.org/assignments/address-family-numbers/address-family-numbers.xhtml
1100. IANA Subsequent Address Family Numbers: https://www.iana.org/assignments/safi-namespace/safi-namespace.xhtml

---

## Useful Commands Cheat Sheet

### Linux/Unix

```bash
# Network interfaces
ip addr show
ip link show
ifconfig -a

# Routes
ip route show
route -n

# MPLS routes (Linux)
ip -f mpls route show
ip -f mpls label show

# Traceroute
traceroute 8.8.8.8
traceroute -I 8.8.8.8
mtr 8.8.8.8

# Ping
ping -c 4 8.8.8.8
ping6 -c 4 2001:4860:4860::8888

# DNS
dig google.com
nslookup google.com
host google.com

# Packet capture
sudo tcpdump -i eth0 -n -w capture.pcap
sudo tcpdump -i eth0 'mpls'
sudo tcpdump -i eth0 'udp port 646'  # LDP
sudo tcpdump -i eth0 'ip proto 46'   # RSVP

# Tshark
tshark -i eth0 -f 'mpls'
tshark -r capture.pcap -Y mpls

# Netstat
ss -tulnp
netstat -tulnp

# Nmap
nmap -sS 192.168.1.0/24
nmap -sV -p 22,23,80,443 target

# Iperf
iperf3 -s
iperf3 -c server_ip

# Bandwidth test
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
```

### Cisco IOS/IOS-XE

```cisco
! Enable MPLS
configure terminal
mpls label protocol ldp
mpls ldp router-id Loopback0 force
interface GigabitEthernet0/0/0
 mpls ip
end

! Verify MPLS
show mpls interfaces
show mpls ldp neighbor
show mpls ldp bindings
show mpls forwarding-table
show mpls ldp discovery
show mpls ldp parameters

! MPLS TE
configure terminal
mpls traffic-eng tunnels
interface Tunnel1
 ip unnumbered Loopback0
 tunnel destination 10.0.0.2
 tunnel mode mpls traffic-eng
 tunnel mpls traffic-eng autoroute announce
 tunnel mpls traffic-eng path-option 1 explicit name PATH1
end

! Verify TE
show mpls traffic-eng tunnels
show mpls traffic-eng topology
show mpls traffic-eng link-management

! L3VPN
vrf definition CUSTOMER
 rd 65000:1
 route-target export 65000:1
 route-target import 65000:1
 address-family ipv4
 exit
exit
router bgp 65000
 address-family ipv4 vrf CUSTOMER
  redistribute connected
 exit
!

! Verify VPN
show ip vrf
show ip route vrf CUSTOMER
show bgp vpnv4 unicast all
show bgp vpnv4 unicast rd 65000:1

! VPLS
l2 vfi CUSTOMER manual
 vpn id 100
 neighbor 10.0.0.2 encapsulation mpls
 neighbor 10.0.0.3 encapsulation mpls

! Verify VPLS
show vfi
show mpls l2transport vc
show xconnect all

! MPLS OAM
ping mpls ipv4 10.0.0.2/32
traceroute mpls ipv4 10.0.0.2/32
```

### Cisco IOS-XR

```cisco
! MPLS LDP
mpls ldp
 router-id 10.0.0.1
 interface Loopback0
 interface GigabitEthernet0/0/0/0

! MPLS TE
mpls traffic-eng
 interface GigabitEthernet0/0/0/0
  admin-weight 1
 interface Tunnel-te1
  ipv4 unnumbered Loopback0
  destination 10.0.0.2
  path-option 1 explicit name PATH1

! Verify
show mpls ldp neighbor
show mpls forwarding
show mpls traffic-eng tunnels
```

### Juniper Junos

```junos
# MPLS LDP
set protocols mpls interface ge-0/0/0.0
set protocols ldp interface ge-0/0/0.0
set protocols ldp interface lo0.0

# MPLS RSVP-TE
set protocols rsvp interface ge-0/0/0.0
set protocols mpls label-switched-path R1-R2 to 10.0.0.2
set protocols mpls interface ge-0/0/0.0

# L3VPN
set routing-instances CUSTOMER instance-type vrf
set routing-instances CUSTOMER interface ge-0/0/1.0
set routing-instances CUSTOMER route-distinguisher 65000:1
set routing-instances CUSTOMER vrf-target target:65000:1

# Verify
show mpls interface
show ldp neighbor
show ldp session
show route table mpls.0
show route table CUSTOMER.inet.0
show rsvp session
show mpls lsp
```

### Nokia SR OS

```nokia
# MPLS LDP
configure router mpls no shutdown
configure router ldp no shutdown
configure router interface "to-R2" mpls-ip
configure router ldp interface-parameters interface "to-R2"

# MPLS RSVP-TE
configure router rsvp no shutdown
configure router mpls no shutdown
configure router mpls path "PATH1" no shutdown
configure router mpls lsp "R1-R2" to 10.0.0.2
configure router mpls lsp "R1-R2" primary "PATH1"

# Verify
show router ldp session
show router ldp bindings
show router mpls interface
show router mpls lsp
show router rsvp session
```

### Arista EOS

```eos
! MPLS
mpls ip
interface Ethernet1
 mpls ip
!
router ldp
 no shutdown

! Verify
show mpls interfaces
show mpls ldp neighbor
show mpls forwarding-table
```

### Huawei VRP

```vrp
# MPLS LDP
mpls lsr-id 10.0.0.1
mpls
mpls ldp
interface GigabitEthernet0/0/1
 mpls
 mpls ldp

# MPLS TE
mpls
mpls te
rsvp
interface GigabitEthernet0/0/1
 mpls te
 rsvp
explicit-path PATH1
 next hop 10.1.1.2
interface Tunnel1
 ip address unnumbered interface LoopBack0
 tunnel-protocol mpls te
 destination 10.0.0.2
 mpls te tunnel-id 1
 mpls te path explicit-path PATH1

# Verify
display mpls interface
display mpls ldp session
display mpls lsp
display mpls te tunnel
```

### MikroTik RouterOS

```mikrotik
# MPLS LDP
/mpls interface add interface=ether1
/mpls ldp set enabled=yes lsr-id=10.0.0.1 transport-address=10.0.0.1
/mpls ldp interface add interface=ether1

# VPLS
/interface vpls add name=vpls1 remote-peer=10.0.0.2 vpls-id=100:1

# Verify
/mpls interface print
/mpls ldp neighbor print
/mpls forwarding-table print
```

### VyOS

```vyos
set protocols mpls interface eth1
set protocols mpls ldp discovery transport-ipv4-address 10.0.0.1
set protocols mpls ldp interface eth1
set protocols mpls ldp router-id 10.0.0.1

commit
save
```

### FRRouting

```frr
! FRR MPLS LDP
mpls ldp
 router-id 10.0.0.1
 address-family ipv4
  discovery transport-address 10.0.0.1
  interface eth1
 exit-address-family
!

! FRR MPLS TE (via pathd/isis)
segment-routing
 traffic-eng
  mpls-te on
  segment-list PATH1
   index 10 mpls-label 100
   index 20 mpls-label 200
```

### Python & Tools

```bash
# Install dependencies
pip install -r requirements.txt

# Run simulator
python mpls_hackers_tchad.py

# CLI mode
python mpls_hackers_tchad.py --cli --topology mesh --nodes 8

# Generate topology graph
python -c "import networkx as nx; g=nx.erdos_renyi_graph(10,0.4); nx.write_gml(g,'topo.gml')"

# Scapy MPLS packet
python - <<'PY'
from scapy.all import *
pkt = Ether()/IP()/MPLS(label=100, ttl=64)/IP(src='10.0.0.1', dst='10.0.0.2')/ICMP()
pkt.show()
wrpcap('mpls_packet.pcap', pkt)
PY
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'tkinter'`

**Solution:** Install Tkinter for your system.

```bash
# Debian/Ubuntu
sudo apt-get install python3-tk

# Fedora/RHEL
sudo dnf install python3-tkinter

# macOS
brew install python-tk

# Windows
# Tkinter is included with the standard Python installer.
```

### Issue: `scapy` requires root for some features

**Solution:** Run with appropriate privileges or install `scapy` without root by using non-privileged packet crafting. The simulator does not require root.

### Issue: 3D view is slow

**Solution:** Reduce node count or disable anti-aliasing in the GUI settings.

### Issue: Label distribution fails

**Solution:** Check that all nodes have unique router IDs and interfaces are enabled.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

- **Project:** MPLS (Hackers_tchad)
- **Community:** Hackers_Tchad
- **Country:** Tchad (Chad)

---

*Merci d'utiliser MPLS (Hackers_tchad). Apprenez, testez, et visualisez MPLS comme un pro !*
