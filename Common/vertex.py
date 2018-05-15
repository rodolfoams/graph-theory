from enum import Enum

class VertexColor(Enum):
    WHITE = 0
    GREY  = 1
    BLACK = 2

class Vertex():
    def __init__(self, name):
        self.name = name
        self.__color = VertexColor.WHITE

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return self.name == other.name and self.__color == other.__color

    def __str__(self):
        return self.name

    def is_white(self):
        return self.__color == VertexColor.WHITE

    def is_grey(self):
        return self.__color == VertexColor.GREY

    def is_black(self):
        return self.__color == VertexColor.BLACK