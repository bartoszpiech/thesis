#!/usr/bin/python
import hashlib
from enum import Enum, auto
from random import randint

MAX_UINT = 4294967295   # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 4       # leading number of zeros in the block hash
BODY_SIZE = 5           # size of transactions in a body


class Blockchain:
    def __init__(self):
        self.blocks = []

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

    def add_transaction(self, transaction):
        if self.blocks[-1].body.add_transaction(transaction) == False:
            self.blocks[-1].compute_hash()
            self.blocks.append(Block(self.blocks[-1].hash.hexdigest()))
            self.add_transaction(transaction)
    #def check_blocks(self):


# TODO add body bounds
class Body:
    def __init__(self):
        self.size = 5
        self.transactions = []
    def __repr__(self):
        return_string = '\n['
        for t in self.transactions:
            return_string += str(t)
        return_string += ']\n'
        return return_string
    def add_transaction(self, transaction):
        if len(self.transactions) < self.size:
            self.transactions.append(transaction)
            return True
        return False

# TODO add list of blocks
class Block:
    def __init__(self, prev_hash = None, special_number = None):
        self.prev_hash = prev_hash
        self.body = Body()
        self.special_number = special_number

    def __repr__(self):
        return '\n(' + str(self.prev_hash) + '|' + str(self.body) + '|' + str(self.special_number) + ')\n'

    def compute_hash(self):
        while True:
            i = randint(1, MAX_UINT)
            self.special_number = i
            h = hashlib.sha256(str(self).encode('utf-8'))
            if check_zeros(h.hexdigest(), LEADING_ZEROS):
                self.special_number = i
                self.hash = h
                d = h.hexdigest()
                return d
    def get_hash(self):
        return hashlib.sha256(str(self).encode('utf-8'))

    def check_zeros(self, number_of_zeros):
        if self[0:number_of_zeros] == '0' * number_of_zeros:
            return True
        return False



# TODO transform transactions into Authentications

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __repr__(self):#works
        return '"' + self.sender + ' sends ' + self.receiver + ' ' \
         + str(self.amount) + 'BD"'

class Con(Enum):
    Open = 1
    Closed = 2

class Authentication:
    def __init__(self, device_id, connection):
        self.device_id = device_id
        self.connection = connection
    def __repr__(self):
        return str(self.connection) + ' - ' + self.device_id + '\n'

def check_zeros(string, number_of_zeros):
    if string[0:number_of_zeros] == '0' * number_of_zeros:
        return True
    return False

a = Authentication('123abc', Con.Open)
print(a)

b = Blockchain()
b.add_block()

for i in range(0,13):
    amount = i
    b.add_transaction(Transaction('Bartek', 'Klaudia', amount))
print(b)

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
