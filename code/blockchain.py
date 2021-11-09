#!/usr/bin/python
import hashlib
import time
from random import randint

MAX_UINT = 4294967295    # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 5       # leading number of zeros in the block hash

# TODO add list of blocks
class Block:
    def __init__(self, prev_hash, transaction, special_number = None):
        self.prev_hash = prev_hash
        self.transaction = transaction
        self.special_number = special_number

    def __repr__(self):
        return str(self.prev_hash) + '|' + str(self.transaction) + '|' + str(self.special_number)

    def find_hash(self):
        while True:
            i = randint(1, MAX_UINT)
            self.special_number = i
            h = hashlib.sha256(str(self).encode('utf-8'))
            if check_zeros(h.hexdigest(), LEADING_ZEROS):
                self.special_number = i
                self.hash = h
                d = h.hexdigest()
                return d

    def check_zeros(self, number_of_zeros):
        if self[0:number_of_zeros] == '0' * number_of_zeros:
            return True
        return False


# TODO add body bounds
class Body:
    def __init__(self, transactions = []):
        self.size = 5
        self.transactions = transactions
    def __repr__(self):
        return_string = ''
        for t in transactions:
            return_string += t
        return return_string

# TODO transform transactions into Authentications
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __repr__(self):
        return '"' + self.sender + ' sends ' + self.receiver + ' ' \
         + str(self.amount) + 'BD"'

def check_zeros(string, number_of_zeros):
    if string[0:number_of_zeros] == '0' * number_of_zeros:
        return True
    return False


t = time.time()
for i in range(0,1000000):
    j = randint(0, MAX_UINT)
    h = hashlib.sha256(str(j).encode('utf-8'))
    if check_zeros(h.hexdigest(), LEADING_ZEROS):
        print(h.hexdigest())
td = time.time() - t
print(td)
