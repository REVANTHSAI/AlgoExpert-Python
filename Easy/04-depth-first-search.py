# Depth First Search - Store all the node names in an array and return it
# Input:
#      A
#   /  |  \
#   B  C   D
# /  \     / \
# E   F   G   H
# Output - [A,B,E,F,C,D,G,H]
# Time - O(V+E) Space - O(V)
# V = Vertives of a graph (Nodes in the graph)
# E = Edges of a Graph (Connections in the graph)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
        for child in self.children:
			child.depthFirstSearch(array)
		return array
