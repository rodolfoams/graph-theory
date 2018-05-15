from graph import Graph
from vertex import Vertex
from utils import *

class Forest():
    def __init__(self, trees=[]):
        if not ( type(trees) is list and check_elements_type(trees, Graph) ):
            raise TypeError("trees must be an iterable that contains only elements of Graph type! Value was: " + str(trees))
        self.trees = list(trees)

    def add_tree(self, new_tree):
        if not isinstance(new_tree, Graph):
            raise TypeError("new_tree must be of Graph type!")
        if self.trees is None:
            self.trees = list()
        self.trees.append(new_tree)

    def remove_tree(self, tree):
        if not isinstance(tree, Graph):
            raise TypeError("tree must be of Graph type!")
        self.trees.remove(tree)

    def __contains__(self, tree):
        for t in self.trees:
            if t == tree:
                return True
        return False

    def __len__(self):
        return len(self.trees)

    def __getitem__(self, idx):
        return self.trees[idx]

    def __str__(self):
        str_builder = ["Forest:"]
        for tree in self.trees:
            str_builder.append(tree.__str__("    "))
        return "\n".join(str_builder)

    def find_tree(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("Argument must be of Graph type!")
        for t in self.trees:
            if vertex in t:
                return t
    
    def merge_trees(self, tree1, tree2):
        if not (isinstance(tree1, Graph) and isinstance(tree2, Graph)):
            raise TypeError("All arguments should be trees!")
        if not (tree1 in self and tree2 in self):
            raise ValueError("One or more trees do not belong to the forest!")
        tree1.V += list(tree2.V)
        tree1.E += list(tree2.E)
        self.trees.remove(tree2)