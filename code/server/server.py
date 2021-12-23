from flask import Flask
from datetime import datetime
import atexit
import threading

from blockchain import *

DEVICE_NUMBER = 1000

app = Flask(__name__)

# mutex prevents from adding new blocks when previous are not full yet (block not fully mined)
mutex = threading.Lock()

# TODO add API that exports all the nodes in separate blocks into one big list

logs = {
        'start': datetime.now().timestamp(),
        'uptime': 0,
        '/api/blockchain': 0,
        '/api/blockchain/height': 0,
        '/api/blockchain/check': 0,
        '/api/open': 0,
        '/api/close': 0,
        '/api/check': 0,
        '/api/logs': 0
        }

# dumps log values to logs.txt file on program shutdown
@atexit.register
def dump_logs():
    logs['uptime'] = datetime.now().timestamp() - logs['start']
    fp = open('logs.txt', 'w')
    fp.write(str(logs))
    fp.close()

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

@app.route('/api/blockchain/check')
def api_blockchain_check():
    logs['/api/blockchain/check'] += 1
    return str(blockchain.check_blocks())

# czy przy dodawaniu/usuwaniu nowego node klient ma czekac az blok zostanie
# znaleziony? czy po prostu zaakceptowac blok i potem w tle sobie szukac hasha?
@app.route('/api/open/<int:dev_id>')
def api_open(dev_id):
    status = 1  # connection open
    global mutex
    logs['/api/open'] += 1
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        return {'Status': 403}
    mutex.acquire()
    n = Node(dev_id, status)
    if blockchain.add_node(n) == False:
        mutex.release()
        return {'Status': 400}
    mutex.release()
    return {'Status': 201}

# czy przy dodawaniu/usuwaniu nowego node klient ma czekac az blok zostanie
# znaleziony? czy po prostu zaakceptowac blok i potem w tle sobie szukac hasha?
# albo po dodaniu ostatniego limitowego node'a blok jest automatycznie kopany?
@app.route('/api/close/<int:dev_id>')
def api_close(dev_id):
    status = 0  # connection open
    global mutex
    logs['/api/close'] += 1
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        return {'Status': 403}
    mutex.acquire()
    n = Node(dev_id, status)
    if blockchain.add_node(n) == False:
        mutex.release()
        return {'Status': 400}
    mutex.release()
    return {'Status': 201}

@app.route('/api/check/<int:dev_id>')
def api_check(dev_id):
    logs['/api/check'] += 1
    if blockchain.check_blocks():       # when blockchain integration is invalid
        return str(blockchain.check_if_authorized(dev_id))
    return False

blockchain = Blockchain()
