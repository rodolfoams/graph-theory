class Edge():
    def __init__(self, weight, origin, destination, directed=False):
        self.weight = weight
        self.origin = origin
        self.destination = destination
        self.directed = directed

    def __gt__(self, other):
        return self.weight > other.weight
    
    def __str__(self):
        arrow = "->" if self.directed else "<->"
        return self.origin.name + arrow + self.destination.name + ", " + str(self.weight)

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        if self.weight != other.weight:
            return False
        if self.origin != other.origin:
            return False
        if self.destination != other.destination:
            return False
        return self.directed == other.directed