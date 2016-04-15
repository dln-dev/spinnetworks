# spinnetworks
Represent spin networks as graphs corresponding to their hamiltonian

The hamiltonian of a system of spins can be interpreted as an adjacency matrix. This program aims to enable the user to input a graph of a network with total spin 1, which is the representation of the network itself, and calculate higher total spin graphs. The sum of all graphs is the graph of the full hamiltonian of the system, which can also be calculated and printed in different formats.

Right now, only homogeneous isotropic chains (J_i ≡1 ) are supported.

Graphs are represented by creating an instance of the spinNetwork class. It needs the number of qubits and the edges in form of a list of tuples containing two vertices. The vertices are powers of two. See example.py for some use cases.
helper.py contains some functions capable of creating edges for often used networks like chains and stars/switches.

Note that this is still a work in progress and nothing was tested rigourously.
