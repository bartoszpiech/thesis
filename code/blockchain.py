import hashlib
from random import randrange

class Block:
    def __init__(self, prev_hash, transaction, special_number):
        self.prev_hash = prev_hash
        self.transaction = transaction
        self.special_number = special_number
    def __repr__(self):
        return str(self.prev_hash) + '|' + str(self.transaction) + '|' + str(self.special_number)

def check_zeros(string, number_of_zeros):
    if string[0:number_of_zeros] == '0' * number_of_zeros:
        return True
    return False

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __repr__(self):
        return '"' + self.sender + ' sends ' + self.receiver + ' ' \
         + str(self.amount) + 'BD"'

amount = 0

checks = 0
while True:
    i = randrange(1, 100000)
    checks = checks + 1
    b = Block(0, Transaction("Bartek", "Klaudia", amount), i)
    h = hashlib.sha256(str(b).encode('utf-8'))
    d = h.hexdigest()
    if check_zeros(d, 3):
        print(i)
        print(d)
        print(b)
        amount = amount + 1
    print(amount)
    if amount == 100:
        print(checks/amount)
        break
