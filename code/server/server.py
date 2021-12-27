from flask import Flask
from datetime import datetime
import atexit
import threading

from blockchain import *

# number of devices in the network
DEVICE_NUMBER = 1000

blockchain = Blockchain('blockchain.json')
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

# increments logs dictionary, saves logs from current session into
# 'logs_file_name' and outputs logs into stderr
def log_and_dump(route, response = ''):
    if response != '':
        response = ', Response: ' + str(response)
    logs_file_name = 'logs.json'
    logs[route] += 1
    app.logger.debug('Request: ' + route + response)
    with open(logs_file_name, 'w') as fp:
        fp.write(str(logs))

@app.route('/api/logs')
def api_logs():
    route = '/api/logs'
    logs['uptime'] = datetime.now().timestamp() - logs['start']
    log_and_dump(route)
    return logs

@app.route('/api/blockchain')
def api_blockchain():
    route = '/api/blockchain'
    log_and_dump(route)
    return str(blockchain.to_json())

@app.route('/api/blockchain/height')
def api_blockchain_height():
    route = '/api/blockchain/height'
    log_and_dump(route, blockchain.get_height())
    return str(blockchain.get_height())

@app.route('/api/blockchain/check')
def api_blockchain_check():
    route = '/api/blockchain/check'
    log_and_dump(route, blockchain.check_integrity())
    return str(blockchain.check_integrity())

@app.route('/api/open/<int:dev_id>')
def api_open(dev_id):
    route = '/api/open'
    connection = 1  # connection open
    status = 201    # status created
    global mutex    # so the blockchain does not add false blocks when multiple
                    # connections come at once
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        status = 403    # status forbidden
    if status == 201:
        mutex.acquire()     # lock stuff
        n = Node(dev_id, connection)
        if blockchain.add_node(n) == False:
            status = 400    # status bad request
        mutex.release()     # unlock stuff
    blockchain.write_to_file()
    log_and_dump(route, status)
    return {'Status': status}

@app.route('/api/close/<int:dev_id>')
def api_close(dev_id):
    route = '/api/close'
    connection = 0  # connection closed
    status = 201    # status created
    global mutex
    if dev_id > DEVICE_NUMBER or dev_id < 0:
        status = 403    # status forbidden
    if status == 201:
        mutex.acquire()     # lock stuff
        n = Node(dev_id, connection)
        if blockchain.add_node(n) == False:
            status = 400    # status bad request
        mutex.release()     # unlock stuff
    blockchain.write_to_file()
    log_and_dump(route, status)
    return {'Status': status}

@app.route('/api/check/<int:dev_id>')
def api_check(dev_id):
    route = '/api/check'
    is_authorized = blockchain.check_if_authorized(dev_id)
    log_and_dump(route, is_authorized)
    return str(is_authorized)
