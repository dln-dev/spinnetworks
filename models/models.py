from operator import xor as opXor
from copy import deepcopy

class spinNetwork():

    def __init__(self,qubits,edges):
        self.__qubits = qubits
        self.__vertices = [ 2**j for j in range(0,self.__qubits) ] # python = <3
        self.__edges = edges

    def __repr__(self):
        return "TBD"

    def __str__(self):
        return "Spin Network of ", self.__qubits, "Qubits with Edges: ", self.getEdges()

    def getQubits(self):
        return self.__qubits

    def getVertices(self,spin=1):
        if spin == 1:
            return self.__vertices
        else:
            vertices = []
            for i in range(0,self.__qubits):
                for j in range(1,self.__qubits-i):
                    vertices += [self.__xor(self.__vertices[i],self.__vertices[i+j])]
            return vertices

    def getEdges(self,spin=1):
        if spin == 1:
            return self.__edges
        else:
            edges = []
            candidates = []
            for vertex in self.getVertices(spin):
                for single in self.__decompose(vertex):
                    for nn in self.__neighbours(single):
                        candidates += [self.__xor(single,nn)]
                for cand in candidates:
                    cand = self.__xor(vertex,cand)
                    if cand != 0:
                        edges += [(vertex,cand)]
                candidates = []
            return edges

    def getFullGraph(self):
        return ["TBD"]

    def getHamiltonian(self,spin=1):
        return ["TBD"]

    def getFullHamiltonian(self):
        return ["TBD"]

    # refuses to work, why?
    #def setEdges(self,edges):
        #self.__edges = deepcopy(edges)

    def __decompose(self,vertex):
        decomp = []
        for i in range(0,self.__qubits):
            if (2**i & vertex):
                decomp += [2**i]
        return decomp

    def __neighbours(self,vertex):
        neighbours = []
        for edge in self.__edges:
            if edge[0] == vertex:
                neighbours += [edge[1]]
        return neighbours

    def __xor(self,*args):
        result = False
        if len(args) >= 2:
            result = args[0]
            for arg in args[1:]:
                result = opXor(result,arg)
        return result
