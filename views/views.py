# prings graph to certain spin up in mathematica format
def mathematicaPrint(spinNetwork,spin=1):
    graphString = ""
    for edge in spinNetwork.getEdges(spin):
        graphString += '"'     + ('{0:0'+str(spinNetwork.getQubits())+'b}').format(edge[0]) \
                    +  '"<->"' + ('{0:0'+str(spinNetwork.getQubits())+'b}').format(edge[1]) + '",'
    print('\ng=Graph[{',graphString[:-1],'},VertexLabels->"Name"]\n',sep='')
