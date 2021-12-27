import hashlib
from datetime import datetime
#from random import randint

from body import *

MAX_UINT = 4294967295   # maximum value of random special number <0, MAX_UINT>
LEADING_ZEROS = 4       # leading number of zeros in the block hash

class Block:
    def __init__(self, prev_hash = '0', special_number = 'None', timestamp = 'None'):
        self.prev_hash = prev_hash
        self.body = Body()
        self.special_number = special_number
        self.timestamp = timestamp

    def __str__(self):
        return str(self.to_json())

    def mine(self):
        for i in range(0, MAX_UINT):
            #i = randint(1, MAX_UINT)    # i -- random, not very efficient
            self.special_number = i
            self.timestamp = datetime.now().timestamp()
            self.hash = hashlib.sha256(str(self).encode('utf-8')).hexdigest()
            if self.check_zeros(LEADING_ZEROS):
                return self.hash

    def to_json(self):
        return {'prev_hash': self.prev_hash, 'body': self.body.to_json(), 'special_number': self.special_number, 'timestamp': self.timestamp}

    def get_hash(self):
        return hashlib.sha256(str(self).encode('utf-8'))

    def check_zeros(self, number_of_zeros):
        if self.get_hash().hexdigest()[0:number_of_zeros] == '0' * number_of_zeros:
            return True
        return False
