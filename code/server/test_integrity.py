from blockchain import *
import time
blockchain = Blockchain('blockchain.json')
start = time.time()
times = 100
for i in range(0,times):
    blockchain.check_integrity()
end = time.time()

print(blockchain.get_height())
print(end - start)
print((end - start) / times / blockchain.get_height())

