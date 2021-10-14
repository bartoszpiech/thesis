import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __repr__(self):
        return str(self.sender) + ';' + str(self.receiver) + ';' + str(self.amount)

class Block:
    def __init__(self, prev_hash):
        self.prev_hash = prev_hash
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __repr__(self):
        return str(self.prev_hash) + ';' + str(self.transactions)

    def hash(self):
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


t1 = Transaction('bartek', 'kuba', 19)
t2 = Transaction('damian', 'kuba', 21)
t3 = Transaction('kuba', 'damian', 36)

b = Block(0)
b.add_transaction(t1)
b.add_transaction(t2)
b.add_transaction(t3)

c = Block(b.hash())
c.add_transaction(t1)
print(b.hash())
print(b)
print(c.hash())
print(c)
