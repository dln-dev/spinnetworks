# prints graph to certain spin up in mathematica format
def mathematicaPrint(spinNetwork,full=False,spin=1):
    width = spinNetwork.getQubits()
    if full:
        graphString = ""
        for edge in spinNetwork.getFullGraph():
            graphString += str(edge[0]) + '<->' + str(edge[1]) + ','
        print('\ng=Graph[{',graphString[:-1],'},VertexLabels->"Name"]\n',sep='')
    else:
        graphString = ""
        for edge in spinNetwork.getEdges(spin):
            graphString += str(edge[0]) + '<->' + str(edge[1]) + ','
        print('\ng=Graph[{',graphString[:-1],'},VertexLabels->"Name"]\n',sep='')



def mathematicaBinaryPrint(spinNetwork,full=False,spin=1):
    width = spinNetwork.getQubits()
    if full:
        graphString = ""
        for edge in spinNetwork.getFullGraph():
            graphString += '"'     + ('{0:0{width}b}').format(edge[0],width=width)[::-1] \
                        +  '"<->"' + ('{0:0{width}b}').format(edge[1],width=width)[::-1] + '",'
        print('\ng=Graph[{',graphString[:-1],'},VertexLabels->"Name"]\n',sep='')
    else:
        graphString = ""
        for edge in spinNetwork.getEdges(spin):
            graphString += '"'     + ('{0:0{width}b}').format(edge[0],width=width)[::-1] \
                        +  '"<->"' + ('{0:0{width}b}').format(edge[1],width=width)[::-1] + '",'
        print('\ng=Graph[{',graphString[:-1],'},VertexLabels->"Name"]\n',sep='')


