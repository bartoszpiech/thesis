import time
import zmq
import requests

IP = 'http://192.168.0.143:5000'

def check_device(dev_id):
    r = requests.get(IP + '/api/check/' + str(dev_id))
    if r.text == 'True':
        return True
    return False


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    incoming_id = int(socket.recv())
    print("Received request: %s" % incoming_id)
    if check_device(incoming_id):
        socket.send(b"+ Device authorized")
    else:
        socket.send(b"- Device unauthorized")
    #time.sleep(1)
