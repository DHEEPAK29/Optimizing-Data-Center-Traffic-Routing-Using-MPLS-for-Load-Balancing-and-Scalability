# Optimizing-Data-Center-Traffic-Routing-Using-MPLS-for-Load-Balancing-and-Scalability
Provisioning Data Center network with MPLS for efficient routing and load balancing between multiple Data Center switches (routers).


1. Network Design: A small Data Center network with multiple switches and servers connected via MPLS-enabled routers. These routers will handle label switching to route packets efficiently.
2. MPLS Configuration: Configuring MPLS, including Label Distribution Protocol (LDP) for label assignment and MPLS forwarding.
3. Load Balancing: Simulating traffic flowing between multiple servers. Improving balance in this load across paths with MPLS.
Py Mininet: Simulating the network and Ryu Controller (OpenFlow) for traffic management.

Tools:
1. Mininet: Network emulator that helps create virtual networks and simulate various network protocols and topologies.
2. Ryu Controller: SDN controller (Py) that can be used to manage OpenFlow-enabled devices and simulate MPLS behavior.
3. Open vSwitch (OVS): Virtual switch to simulate MPLS behavior.

Textual Representation of the network Used: 

   dc1 ---- dc2 ---- dc3
    |       |       |
   h1      h2      h3

MPLS labels, the Ryu Controller dynamically adjusts the paths based on network conditions (e.g., link failure, congestion).
Key Features:
- MPLS in Data Center: This setup uses MPLS labels to forward packets between data center switches, which improves scalability and reduces latency.
- Dynamic Load Balancing: Traffic can be distributed efficiently across different paths using MPLS and SDN controllers.
- Fault Tolerance: If a link fails, the SDN controller can reroute traffic based on MPLS labels, ensuring high availability.
- Scalability: The MPLS-based approach allows easy addition of new data center switches and servers, as the network grows.
