#!/usr/bin/python
import hashlib
from random import randint

from block import Block

MAX_UINT = 4294967295   # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 4       # leading number of zeros in the block hash
BODY_SIZE = 5           # size of transactions in a body

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
        if self.blocks[-1].body.add_node(node) == False:
            self.blocks[-1].compute_hash()
            self.blocks.append(Block(self.blocks[-1].hash))
            self.add_node(node)

    def check_blocks(self):
        # loop over all blocks except the last one (dont know if its mined yet)
        for i, block in enumerate(self.blocks[:-1]):
            print('actual hash:' + block.get_hash().hexdigest())
            print('prev hash:' + self.blocks[i + 1].prev_hash)
            print('check_zeros:' + str(block.check_zeros(LEADING_ZEROS)))
            if block.get_hash().hexdigest() != self.blocks[i + 1].prev_hash or block.check_zeros(LEADING_ZEROS) == False:
                return False
        return True

    def get_height(self):
        return len(self.blocks) - 1


if __name__ == '__main__':
    blockchain = Blockchain()
    for i in range(0,25):
        t = Node(randint(0,100), randint(0,1))
        blockchain.add_node(t)
        print(blockchain)
