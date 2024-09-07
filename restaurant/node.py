class Node:
    def __init__(self, name, price=None, description=None, category=None):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.edges = []
        self.reverse_edges = []

    def add_edge(self, node):
        self.edges.append(node)
        node.reverse_edges.append(self)

    def get_edges(self):
        return self.edges

    def get_reverse_edges(self):
        return self.reverse_edges
