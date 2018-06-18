import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "Common"))
from vertex import Vertex, VertexColor
from edge import Edge
from graph import Graph

visited = None

def dfs(G, current, target):
    global visited
    if visited is None: visited = list()
    current.set_color(VertexColor.BLACK)
    visited.append(current)
    if current == target:
        return True
    for e in G.E:
        if e.origin == current and e.destination.has_color(VertexColor.WHITE):
            if dfs(G, e.destination, target): return True
        elif e.destination == current and e.origin.has_color(VertexColor.WHITE):
            if dfs(G, e.origin, target): return True
    return False

def main(args):
    global visited
    V = [Vertex("0"), Vertex("1"), Vertex("2"), Vertex("3"), Vertex("4"), Vertex("5"), Vertex("6"), Vertex("7"), Vertex("8"), Vertex("9"), Vertex("10"), Vertex("11"), Vertex("12"), Vertex("13"), Vertex("14")]
    E = [Edge(1,V[0],V[1]), Edge(1,V[0],V[2]), Edge(1,V[1],V[3]), Edge(1,V[1],V[4]), Edge(1,V[3],V[7]), Edge(1,V[3],V[8]), Edge(1,V[4],V[9]), Edge(1,V[4],V[10]), Edge(1,V[2],V[5]), Edge(1,V[2],V[6]), Edge(1,V[5],V[11]), Edge(1,V[5],V[12]), Edge(1,V[6],V[13]), Edge(1,V[6],V[14])]
    G = Graph(V, E)
    '''
                                    0
                            /               \
                    1                               2
                /       \                       /       \
            3               4               5               6
          /   \           /   \           /   \           /   \
        7       8       9       10      11      12      13      14
    '''
    visited = list()
    assert(dfs(G, V[0], V[12]) == True)
    assert(len(visited) == 12)
    print(map(str,visited))

if __name__ == "__main__":
    main(sys.argv[1:])