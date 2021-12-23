#!/usr/bin/python
import hashlib
from random import randint

from block import *


class Blockchain:
    def __init__(self):
        self.blocks = []
        self.add_block()

    def to_json(self):
        tmp = []
        for block in self.blocks:
            tmp.append(block.to_json())
        return {'blocks': tmp}

    def add_block(self):
        if len(self.blocks) == 0:
            self.blocks.append(Block())
        else:
            block.prev_hash = self.blocks[-1]
            self.blocks.append(Block())

    def add_node(self, node):
        authorized = self.get_authorized()
        if node.connection_status == 0 and node.device_id not in authorized:
            return False
        if node.connection_status == 1 and node.device_id in authorized:
            return False
        if self.blocks[-1].body.add_node(node) == False:
            hash = self.blocks[-1].mine()
            self.blocks.append(Block(hash))
            self.add_node(node)
        return True

    def check_blocks(self):
        # loop over all blocks except the last one (dont know if its mined yet)
        for i in range(len(self.blocks) - 1):
            print('actual hash:' + self.blocks[i].get_hash().hexdigest())
            print('prev hash:' + self.blocks[i + 1].prev_hash)
            print('check_zeros:' + str(self.blocks[i].check_zeros(LEADING_ZEROS)))
            if self.blocks[i].get_hash().hexdigest() != self.blocks[i + 1].prev_hash or self.blocks[i].check_zeros(LEADING_ZEROS) == False:
                return False
        return True

    # unwrap all blocks into one list of nodes
    def unwrap(self):
        nodes = []
        for i in self.blocks:
            nodes += i.body.nodes
        return nodes

    # get devices that are authorized in the blockchain
    def get_authorized(self):
        authorized = []
        nodes = self.unwrap()
        for n in nodes:
            if n.connection_status == 1 and n.device_id not in authorized:
                authorized.append(n.device_id)
            if n.connection_status == 0 and n.device_id in authorized:
                authorized.remove(n.device_id)
        return authorized

    def check_if_authorized(self, dev_id):
        if dev_id in self.get_authorized():
            return True
        return False


    def get_height(self):
        return len(self.blocks) - 1

"""
def to_json(l):
    result_string = '{'
    for i in l:
        result_string += str(i)
    result_string += '}'
    return result_string
"""

"""
def main():
    blockchain = Blockchain()
    for i in range(0,25):
        t = Node(randint(0,100), randint(0,1))
        blockchain.add_node(t)
        print(blockchain)
"""

if __name__ == '__main__':
    blockchain = Blockchain()
    for i in range(0,25):
        t = Node(randint(0,100), randint(0,1))
        if blockchain.add_node(t) == False:
            print('nie udalo sie dodac node')
        print(blockchain)
