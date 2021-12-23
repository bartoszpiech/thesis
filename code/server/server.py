from flask import Flask
from datetime import datetime
import atexit
import threading

from blockchain import *

# number of devices in the network
DEVICE_NUMBER = 1000

app = Flask(__name__)

# mutex prevents from adding new blocks when previous are not full yet (block not fully mined)
mutex = threading.Lock()

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

# TODO bug, does not work for now
# dumps log values to logs.txt file on program shutdown
@atexit.register
def dump_logs():
    #global logs
    #logs['uptime'] = datetime.now().timestamp() - logs['start']
    with open('logs.txt', 'w') as fp:
        fp.write(str(logs))

@app.route('/api/logs')
def api_logs():
    logs['uptime'] = datetime.now().timestamp() - logs['start']
    logs['/api/logs'] += 1
    app.logger.debug('Request /api/logs')
    return logs

@app.route('/api/blockchain')
def api_blockchain():
    logs['/api/blockchain'] += 1
    app.logger.debug('Request /api/blockchain')
    return blockchain.to_json()

@app.route('/api/blockchain/height')
def api_blockchain_height():
    logs['/api/blockchain/height'] += 1
    app.logger.debug('Request /api/blockchain/height')
    return str(blockchain.get_height())

@app.route('/api/blockchain/check')
def api_blockchain_check():
    logs['/api/blockchain/check'] += 1
    app.logger.debug('Request /api/blockchain/check')
    return str(blockchain.check_blocks())

@app.route('/api/open/<int:dev_id>')
def api_open(dev_id):
    connection = 1  # connection open
    status = 201
    global mutex
    logs['/api/open'] += 1
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        status = 403
    if status == 201:
        mutex.acquire()
        n = Node(dev_id, connection)
        if blockchain.add_node(n) == False:
            status = 400
        mutex.release()
    app.logger.debug('Request /api/open/' + str(dev_id) + ' -- Response: ' + str(status))
    return {'Status': status}

@app.route('/api/close/<int:dev_id>')
def api_close(dev_id):
    connection = 0  # connection closed
    status = 201
    global mutex
    logs['/api/open'] += 1
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        status = 403
    if status == 201:
        mutex.acquire()
        n = Node(dev_id, connection)
        if blockchain.add_node(n) == False:
            status = 400
        mutex.release()
    app.logger.debug('Request /api/close/' + str(dev_id) + ' -- Response: ' + str(status))
    return {'Status': status}

@app.route('/api/check/<int:dev_id>')
def api_check(dev_id):
    is_authorized = blockchain.check_if_authorized(dev_id) and blockchain.check_blocks()
    logs['/api/check'] += 1
    app.logger.debug('Request /api/check/' + str(dev_id) + ' -- Response: ' + str(is_authorized))
    return str(is_authorized)

blockchain = Blockchain()
