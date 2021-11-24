#!/usr/bin/python
import hashlib
from enum import Enum, auto
from random import randint

from flask import Flask
app = Flask(__name__)

MAX_UINT = 4294967295   # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 5       # leading number of zeros in the block hash
BODY_SIZE = 5           # size of transactions in a body

# TODO add API that exports all the nodes in separate blocks into one big list
# TODO classes as separate files
# TODO check blocks
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
    #def check_blocks(self):

class Body:
    def __init__(self):
        self.size = 5
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

class Block:
    def __init__(self, prev_hash = 0, special_number = None):
        self.prev_hash = prev_hash
        self.body = Body()
        self.special_number = special_number

    def compute_hash(self):
        for i in range(0, MAX_UINT):
            #i = randint(1, MAX_UINT)    # i -- random, not very efficient
            self.special_number = i
            self.hash = hashlib.sha256(str(self.to_json()).encode('utf-8')).hexdigest()
            if self.check_zeros(LEADING_ZEROS):
                return self.hash

    def to_json(self):
        return {'prev_hash': self.prev_hash, 'body': self.body.to_json(), 'special_number': self.special_number}

    def get_hash(self):
        return hashlib.sha256(str(self).encode('utf-8'))

    def check_zeros(self, number_of_zeros):
        if self.hash[0:number_of_zeros] == '0' * number_of_zeros:
            return True
        return False

# Tutaj mialem problemy przy tworzeniu connection status jako enuma, zamiast
# tego dalem int, 0 -> otwarte polaczenia, 1 -> zamkniete polaczenia.
class Node:
    def __init__(self, device_id, connection_status):
        self.device_id = device_id
        self.connection_status = connection_status  # 1 -- open, 0 -- closed

    def to_json(self):
        return {'device_id': self.device_id, 'connection_status': self.connection_status}

def check_zeros(string, number_of_zeros):
    if string[0:number_of_zeros] == '0' * number_of_zeros:
        return True
    return False


@app.route('/api/blockchain')
def api_blockchain():
    #app.logger.debug('BLOCKCHAIN' + str(blockchain.to_json()))
    return blockchain.to_json()

# czy przy dodawaniu/usuwaniu nowego node klient ma czekac az blok zostanie
# znaleziony? czy po prostu zaakceptowac blok i potem w tle sobie szukac hasha?
@app.route('/api/open/<int:dev_id>')
def api_open(dev_id):
    status = 1  # connection open
    if dev_id > 999 or dev_id < 0:
        return {'Status': 403}
    n = Node(dev_id, status)
    blockchain.add_node(n)
    return {'Status': 201}

# czy przy dodawaniu/usuwaniu nowego node klient ma czekac az blok zostanie
# znaleziony? czy po prostu zaakceptowac blok i potem w tle sobie szukac hasha?
@app.route('/api/close/<int:dev_id>')
def api_close(dev_id):
    status = 0  # connection open
    if dev_id > 999 or dev_id < 0:
        return {'Status': 403}
    n = Node(dev_id, status)
    blockchain.add_node(n)
    return {'Status': 201}

blockchain = Blockchain()

# tego chyba sie we flasku nie daje
# ...
if __name__ == '__main__':
    print('siema')
