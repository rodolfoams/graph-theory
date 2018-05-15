from sys import argv

class Vertex():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class Edge():
    def __init__(self, weight, origin, destination):
        self.weight = weight
        self.origin = origin
        self.destination = destination

    def __gt__(self, other):
        return self.weight > other.weight
    
    def __str__(self):
        return self.origin.name + "<->" + self.destination.name

def get_safe_edges(visited, E):
    safe_edges = list()
    for e in E:
        if e.origin in visited and e.destination not in visited:
            safe_edges.append(e)
        if e.destination in visited and e.origin not in visited:
            safe_edges.append(e)
    return safe_edges

def prim(V, E):
    visited = [V[0]]
    to_visit = list(V)
    to_visit.remove(V[0])
    chosen_edges = list()
    safe_edges = get_safe_edges(visited, E)
    while len(to_visit) > 0:
        safe_edges.sort()
        chosen_edge = safe_edges[0]
        v = chosen_edge.origin if chosen_edge.origin not in visited else chosen_edge.destination
        chosen_edges.append(chosen_edge)
        visited.append(v)
        to_visit.remove(v)
        safe_edges = get_safe_edges(visited, E)
    return chosen_edges

def main(args):
    V = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E")]
    E = [Edge(9,V[0],V[1]), Edge(5,V[0],V[2]), Edge(10,V[0],V[4]), Edge(1,V[1],V[3]), Edge(11,V[2],V[3])]
    MST = prim(V, E)
    for e in MST:
        print e

if __name__ == "__main__":
    main(argv[1:])