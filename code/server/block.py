import hashlib
#from random import randint

from body import Body

# TODO dodanie pola is_mined do klasy block zeby wiedziec czy i kiedy zostal
# wykopany, dodanie timestampa z wykopania



class Block:
    def __init__(self, prev_hash = 0, special_number = None):
        self.prev_hash = prev_hash
        self.body = Body()
        self.special_number = special_number

    def __str__(self):
        return str(self.to_json())

    def compute_hash(self):
        for i in range(0, MAX_UINT):
            #i = randint(1, MAX_UINT)    # i -- random, not very efficient
            self.special_number = i
            self.hash = hashlib.sha256(str(self).encode('utf-8')).hexdigest()
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
