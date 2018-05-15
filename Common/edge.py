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