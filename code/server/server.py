import functools
from flask import Flask
import atexit

from blockchain import Blockchain

app = Flask(__name__)

# TODO add API that exports all the nodes in separate blocks into one big list


def invocation_counter(func):
    inv_counter = 0

    @functools.wraps(func)
    def decorating_function(*args, **kwargs):
        nonlocal inv_counter
        inv_counter += 1
        func(*args, **kwargs)

    def info():
        return inv_counter

    def clear():
        inv_counter = 0

    decorating_function.clear = clear
    decorating_function.info = info
    return decorating_function

@atexit.register
def log():
    print('Logs:\n')
    print(api_blockchain.info())


@invocation_counter
@app.route('/api/blockchain')
def api_blockchain():
    #app.logger.debug('BLOCKCHAIN' + str(blockchain.to_json()))
    return blockchain.to_json()

@app.route('/api/blockchain/height')
def api_blockchain_height():
    return str(blockchain.get_height())

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
# albo po dodaniu ostatniego limitowego node'a blok jest automatycznie kopany?
@app.route('/api/close/<int:dev_id>')
def api_close(dev_id):
    status = 0  # connection open
    if dev_id > 999 or dev_id < 0:
        return {'Status': 403}
    n = Node(dev_id, status)
    blockchain.add_node(n)
    return {'Status': 201}

blockchain = Blockchain()
