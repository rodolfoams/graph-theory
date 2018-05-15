class Edge():
    def __init__(self, weight, origin, destination):
        self.weight = weight
        self.origin = origin
        self.destination = destination

    def __gt__(self, other):
        return self.weight > other.weight
    
    def __str__(self):
        return self.origin.name + "<->" + self.destination.name