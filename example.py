import spinNetworks as sn

graph = sn.spinNetwork(4,sn.chainEdges(4))
print(graph.getVertices(4))
print(graph.getEdges(2))

sn.mathematicaPrint(graph)

switch = sn.spinNetwork(4,sn.switchEdges(4))
print(switch.getVertices(2))
print(switch.getEdges(2))

sn.mathematicaBinaryPrint(switch)

graph_manual = sn.spinNetwork(5,[(1,2),(2,4),(2,8),(4,8),(4,16),(8,16)])
print(graph_manual.getEdges(2))
print(graph_manual.getEdges(3))

sn.mathematicaPrint(graph_manual,True)
