#!/usr/bin/python
import hashlib
from random import randint
import json

from block import *

class Blockchain:
    def __init__(self, file_name = None):
        self.blocks = []
        self.file_name = file_name
        if isinstance(self.file_name, str):
            if not self.read_from_file():
                print(f'File {self.file_name} not found, creating one.')
                self.add_block()
                self.write_to_file()
            elif self.check_integrity():
                print(f'Read blockchain from file {self.file_name} successful, blockchain integrity not violated.')
            else:
                print('Error: Blockchain integrity violated!')
                exit(1)
        if len(self.blocks) == 0:
            self.add_block()

    def to_json(self):
        tmp = []
        for block in self.blocks:
            tmp.append(block.to_json())
        return {'blocks': tmp}

    def write_to_file(self):
        with open(self.file_name, 'w') as fp:
            fp.write(str(self.to_json()))

    def read_from_file(self):
        try:
            with open(self.file_name, 'r') as fp:
                blockchain_str = fp.read()
        except FileNotFoundError:
            return False
        json_blockchain = json.loads(blockchain_str.replace("'", "\""))
        for block in json_blockchain['blocks']:
            body = Body()
            for node in block['body']['nodes']:
                body.add_node(Node(node['device_id'], node['connection_status']))
            self.blocks.append(Block(str(block['prev_hash']), block['special_number'], block['timestamp']))
            self.blocks[-1].body = body
        return True

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

    def check_integrity(self):
        # loop over all blocks except the last one (dont know if its mined yet)
        for i in range(len(self.blocks) - 1):
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
if __name__ == '__main__':
    blockchain = Blockchain()
    for i in range(0,25):
        t = Node(randint(0,100), randint(0,1))
        if blockchain.add_node(t) == False:
            print('nie udalo sie dodac node')
"""
