#!/usr/bin/python
import hashlib
from enum import Enum, auto
from random import randint

from flask import Flask
app = Flask(__name__)

MAX_UINT = 4294967295   # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 5       # leading number of zeros in the block hash
BODY_SIZE = 5           # size of transactions in a body


# TODO check blocks
class Blockchain:
    def __init__(self):
        self.blocks = []
        self.add_block()

    def __repr__(self):
        return_string = '\n{'
        for b in self.blocks:
            return_string += str(b)
        return_string += '}\n'
        return return_string

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

    def __repr__(self):
        return_string = '\n['
        for t in self.nodes:
            return_string += str(t)
        return_string += ']\n'
        return return_string

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

    def __repr__(self):
        return '\n(' + str(self.prev_hash) + '|' + str(self.body) + '|' + str(self.special_number) + ')\n'

    def compute_hash(self):
        while True:
            i = randint(1, MAX_UINT)
            self.special_number = i
            self.hash = hashlib.sha256(str(self).encode('utf-8')).hexdigest()
            if self.check_zeros(LEADING_ZEROS):
                return self.hash

    def get_hash(self):
        return hashlib.sha256(str(self).encode('utf-8'))

    def check_zeros(self, number_of_zeros):
        if self.hash[0:number_of_zeros] == '0' * number_of_zeros:
            return True
        return False

# TODO transform transactions into Authentications
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __repr__(self):
        return '"' + self.sender + ' sends ' + self.receiver + ' ' \
         + str(self.amount) + 'BD"'

# TODOO connection status as enum, did not work earlier because enum cannot 
# be converted easily to dict as part of another object
class Node:
    def __init__(self, device_id, connection_status):
        self.device_id = device_id
        self.connection_status = connection_status  # 1 -- open, 0 -- closed
    def __repr__(self):
        return str(self.connection_status) + ' - ' + str(self.device_id)

def check_zeros(string, number_of_zeros):
    if string[0:number_of_zeros] == '0' * number_of_zeros:
        return True
    return False


@app.route('/api/node')
def api():
    n = Node(randint(0,100), randint(0, 1))
    app.logger.debug('new node request: ' + str(n.__dict__))
    return n.__dict__

l = []
@app.route('/api/add/<int:dev_id>/<int:status>')
def api_add_node(dev_id, status):
    app.logger.debug('API ADD: ' + str(dev_id) + ' ' + str(status))
    if status != 1 and status != 0:
        return {'Status': 403}
    n = Node(dev_id, status)
    l.append(n)
    app.logger.debug('LIST:' + str(l))

    return {'Status': 201}

""" blockchain test -- 13 nodes added
b = Blockchain()

for i in range(0,13):
    t = (randint(0,100), Con.Open)
    b.add_node(t)
print(b)
"""

"""
body = Body()
for i in range(1,10):
    works = body.add_transaction('siema' + str(i))
    print(works)
print(body.transactions)
"""
"""
amount = 0
b = Block(0, Transaction("Bartek", "Klaudia", amount))
d = b.compute_hash()
print(b)
print(d)
"""
