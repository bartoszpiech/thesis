import time
import zmq
import requests
from random import randrange

IP = 'http://192.168.0.164:5000'

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
    if check_device(incoming_id):
        temperature = randrange(-20, 40)
        brightness = randrange(0, 100)
        socket.send_string(f"Device {incoming_id} authorized: {temperature} {brightness}")
        print(f"Received request from : {incoming_id} -- authorized, Response: {temperature} {brightness}")
    else:
        print(f"Received request from : {incoming_id} -- unauthorized")

""" for benchmark purpose
# Code without server check
while True:
    incoming_id = int(socket.recv())
    temperature = randrange(-20, 40)
    brightness = randrange(0, 100)
    socket.send_string(f"Device {incoming_id} authorized: {temperature} {brightness}")
    print(f"Received request from : {incoming_id} -- authorized, Response: {temperature} {brightness}")
"""
