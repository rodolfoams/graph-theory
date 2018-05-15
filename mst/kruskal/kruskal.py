import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "Common"))
from vertex import Vertex
from edge import Edge
from graph import Graph
from forest import Forest

def get_safe_edges(visited, E):
    safe_edges = list()
    for e in E:
        if e.origin in visited and e.destination not in visited:
            safe_edges.append(e)
        if e.destination in visited and e.origin not in visited:
            safe_edges.append(e)
    return safe_edges

def kruskal(G):
    forest = Forest(map(lambda x: Graph([x]),G.V))
    edges = sorted(G.E)
    for e in edges:
        if len(forest) == 1:
            break
        t1 = forest.find_tree(e.origin)
        t2 = forest.find_tree(e.destination)
        if t1 == t2:
            continue
        forest.merge_trees(t1, t2)
        t1.add_edge(e)
    return forest[0]

def main(args):
    V = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E")]
    E = [Edge(9,V[0],V[1]), Edge(5,V[0],V[2]), Edge(10,V[0],V[4]), Edge(1,V[1],V[3]), Edge(11,V[2],V[3])]
    G = Graph(V, E)
    MST = kruskal(G)
    print "================= Original Graph ======================"
    print G
    print "================= MST ======================"
    print MST

if __name__ == "__main__":
    main(sys.argv[1:])