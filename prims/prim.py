import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Common"))
from vertex import Vertex
from edge import Edge
from graph import Graph
# from graph import Graph

def get_safe_edges(visited, E):
    safe_edges = list()
    for e in E:
        if e.origin in visited and e.destination not in visited:
            safe_edges.append(e)
        if e.destination in visited and e.origin not in visited:
            safe_edges.append(e)
    return safe_edges

def prim(G):
    MST = Graph(G.V)
    V = G.V
    E = G.E
    visited = [V[0]]
    to_visit = list(V)
    to_visit.remove(V[0])
    safe_edges = get_safe_edges(visited, E)
    while len(to_visit) > 0:
        safe_edges.sort()
        chosen_edge = safe_edges[0]
        v = chosen_edge.origin if chosen_edge.origin not in visited else chosen_edge.destination
        MST.add_edge(chosen_edge)
        visited.append(v)
        to_visit.remove(v)
        safe_edges = get_safe_edges(visited, E)
    return MST

def main(args):
    V = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E")]
    E = [Edge(9,V[0],V[1]), Edge(5,V[0],V[2]), Edge(10,V[0],V[4]), Edge(1,V[1],V[3]), Edge(11,V[2],V[3])]
    G = Graph(V, E)
    MST = prim(G)
    print "================= Original Graph ======================"
    print G
    print "================= MST ======================"
    print MST

if __name__ == "__main__":
    main(sys.argv[1:])