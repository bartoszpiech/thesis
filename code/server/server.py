from flask import Flask
from datetime import datetime
import atexit

from blockchain import Blockchain
from node import Node

app = Flask(__name__)

# TODO add API that exports all the nodes in separate blocks into one big list

logs = {
        'start': datetime.now().timestamp(),
        'uptime': 0,
        '/api/blockchain': 0,
        '/api/blockchain/height': 0,
        '/api/open': 0,
        '/api/close': 0,
        '/api/logs': 0
        }

# dumps log values to logs.txt file on program shutdown
@atexit.register
def dump_logs():
    logs['uptime'] = datetime.now().timestamp() - logs['start']
    fp = open('logs.txt', 'w')
    fp.write(str(logs))
    fp.close()

#
@app.route('/api/logs')
def api_logs():
    logs['uptime'] = datetime.now().timestamp() - logs['start']
    logs['/api/logs'] += 1
    return logs

@app.route('/api/blockchain')
def api_blockchain():
    logs['/api/blockchain'] += 1
#app.logger.debug('BLOCKCHAIN' + str(blockchain.to_json()))
    return blockchain.to_json()

@app.route('/api/blockchain/height')
def api_blockchain_height():
    logs['/api/blockchain/height'] += 1
    return str(blockchain.get_height())

# czy przy dodawaniu/usuwaniu nowego node klient ma czekac az blok zostanie
# znaleziony? czy po prostu zaakceptowac blok i potem w tle sobie szukac hasha?
@app.route('/api/open/<int:dev_id>')
def api_open(dev_id):
    logs['/api/open'] += 1
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
    logs['/api/close'] += 1
    status = 0  # connection open
    if dev_id > 999 or dev_id < 0:
        return {'Status': 403}
    n = Node(dev_id, status)
    blockchain.add_node(n)
    return {'Status': 201}

blockchain = Blockchain()
