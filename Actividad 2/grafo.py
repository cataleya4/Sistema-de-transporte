class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].neighbors[node2] = weight
        self.nodes[node2].neighbors[node1] = weight

class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.neighbors = {}
