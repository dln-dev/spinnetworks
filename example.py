import spinNetworks as sn

graph = sn.spinNetwork(4,sn.chainEdges(4))
graph.getVertices(2)
graph.getEdges(2)

sn.mathematicaPrint(graph)
