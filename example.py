import spinNetworks as sn

graph = sn.spinNetwork(4,sn.chainEdges(4))
print(graph.getVertices(4))
print(graph.getEdges(2))

sn.mathematicaPrint(graph)

switch = sn.spinNetwork(4,sn.switchEdges(4))
print(switch.getVertices(2))
print(switch.getEdges(2))

sn.mathematicaPrint(switch)
