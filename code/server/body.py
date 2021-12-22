from node import Node

BODY_SIZE = 5           # size of transactions in a body

class Body:
    def __init__(self):
        self.size = BODY_SIZE
        self.nodes = []

    def to_json(self):
        tmp = []
        for node in self.nodes:
            tmp.append(node.to_json())
        return {'size': self.size, 'nodes': tmp}

    def add_node(self, node):
        if len(self.nodes) < self.size:
            self.nodes.append(node)
            return True
        return False
