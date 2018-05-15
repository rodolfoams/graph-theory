from vertex import Vertex
from edge import Edge
from utils import *

class Graph():
    def __init__(self, V=[], E=[]):
        if not ( type(V) is list and check_elements_type(V, Vertex) ):
            raise TypeError("V must be an iterable that contains only elements of type Vertex! Value was: " + str(V))
        self.V = list(V)
        if not ( type(E) is list and check_elements_type(E, Edge) ):
            raise TypeError("E must be an iterable that contains only elements of type Edge! Value was: " + str(E))
        self.E = list(E)

    def __str__(self, indent=""):
        str_builder = ["Graph:", "    Vertices:"]
        str_builder.append("        " + ",".join(map(str, self.V)))
        str_builder.append("    Edges:")
        for e in self.E:
            str_builder.append("        " + str(e))  
        return "\n".join(map(lambda x: indent + x, str_builder))

    def __eq__(self, other):
        if not isinstance(other, Graph):
            return False
        for v in self.V:
            if v not in other.V:
                return False
        for v2 in other.V:
            if v2 not in self.V:
                return False
        for e in self.E:
            if e not in other.E:
                return False
        for e2 in self.E:
            if e2 not in self.E:
                return False
        return True

    def __contains__(self, obj):
        if isinstance(obj, Vertex):
            return obj in self.V
        if isinstance(obj, Edge):
            return obj in self.E
        return False
    
    def add_vertex(self, new_vertex):
        if not isinstance(new_vertex, Vertex):
            raise TypeError("new_vertex must be of Vertex type!")
        if self.V is None:
            self.V = list()
        self.V.append(new_vertex)

    def remove_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("vertex must be of Vertex type!")
        self.V.remove(vertex)

    def add_edge(self, new_edge):
        if not isinstance(new_edge, Edge):
            raise TypeError("new_edge must be of Edge type!")
        if self.E is None:
            self.E = list()
        self.E.append(new_edge)

    def remove_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError("edge must be of Edge type!")
        self.V.remove(edge)