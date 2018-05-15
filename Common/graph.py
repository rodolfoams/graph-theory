from vertex import Vertex
from edge import Edge
from utils import *

class Graph():
    def __init__(self, V=[], E=[]):
        if not ( type(V) is list and check_elements_type(V, Vertex) ):
            raise TypeError("All elements V must be of type Vertex!")
        self.V = V
        if not ( type(E) is list and check_elements_type(E, Edge) ):
            raise TypeError("All elements E must be of type Edge!")
        self.E = E
    
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
        if self.V is None:
            self.V = list()
        self.V.append(new_edge)

    def remove_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError("edge must be of Edge type!")
        self.V.remove(edge)