# generates edges for a simple spin chain
def chainEdges(qubits,periodic=False):
    vertices = [ 2**j for j in range(0,qubits) ]
    edges = [ (vertices[i],vertices[i+1]) for i in range(0,qubits-1) ]
    if periodic:
        edges += [(vertices[qubits-1],vertices[0])]
    return edges
