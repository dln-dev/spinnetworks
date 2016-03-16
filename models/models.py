from operator import xor as opXor
from itertools import combinations

class spinNetwork():

    def __init__(self,qubits,edges):
        self.__qubits = qubits
        self.__vertices = [ 2**j for j in range(0,self.__qubits) ] # python = <3
        self.__edges = edges

    def __repr__(self):
        return "TBD"

    def __str__(self):
        return "Spin Network of " + str(self.__qubits) \
             + " Qubits with Edges: " + str(self.getEdges())

    def getQubits(self):
        return self.__qubits

    def getVertices(self,spin=1):
        if spin == 1:
            return self.__vertices
        elif spin == 0:
            return [0]
        elif spin == self.__qubits:
            return [2**self.__qubits-1]
        elif spin >= 1:
            vertices = []
            for combination in combinations(self.__vertices, spin):
                vertices += [self.__xor(list(combination))]
            return vertices
        else:
            return []

    def getEdges(self,spin=1):
        if spin == 1:
            return self.__edges
        elif spin == 0:
            return [(0,0)]
        elif spin == self.__qubits:
            return [(2**self.__qubits-1,2**self.__qubits-1)]
        elif spin >= 1:
            edges = []
            candidates = []
            for vertex in self.getVertices(spin):
                dec = self.__decompose(vertex)
                for comb in combinations(dec,spin-1):
                    # neighbours of element in dec not in comb, needs improvement
                    neighbours = self.__neighbours([x for x in dec if x not in comb][0])
                    for nn in neighbours:
                        if nn not in comb:
                            edges += [(vertex,self.__xor(list(comb)+[nn]))]
                neighbours = []
            decomposition = []
            return edges
        else:
            return []
            
    def getFullGraph(self):
        edges = []
        for i in range(0,self.__qubits+1):
            edges += self.getEdges(i)
        return edges

    def getHamiltonian(self,spin=1):
        return ["TBD"]

    def getFullHamiltonian(self):
        return ["TBD"]

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
        
    # takes list of arguments and xors all elements
    def __xor(self, args):
        if len(args) > 1:
            result = args[0]
            for arg in args[1:]:
                result = opXor(result,arg)
            return result
        else:
            return args[0]
