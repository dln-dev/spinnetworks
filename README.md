# spinnetworks
Represent spin networks as graphs corresponding to their hamiltonian

The hamiltonian of a system of spins can be interpreted as an adjacency matrix. This program aims to enable the user to input a graph of a network with total spin 1, which is the representation of the network itself, and calculate higher stotal spin graphs. The sum of all graphs is the graph of the full hamiltonian of the system, which can also be calculated and printed in different formats.

Right now, only homogeneous isotropic chains (J_i ≡1 ) are supported. Only spin=1 and spin=2 graphs can be calculated.

Note that this is still a work in progress and nothing was tested rigourously.

Usage example:

import spinNetworks as sn

graph = sn.spinNetwork(4,sn.chainEdges(4))
graph.getEdges(1)
graph.getEdges(2)

mathematicaPrint(graph,2)
