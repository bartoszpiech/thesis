#!/usr/bin/python

import sys
import zmq
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://localhost:5555')
node_filter = sys.argv[1] if len(sys.argv) > 1 else "1"
socket.setsockopt_string(zmq.SUBSCRIBE, node_filter)
print('Subscribing to node: ' + str(node_filter) + ' on localhost:5555')

while (True):
    string = socket.recv_string()
    node, temperature, brightness = string.split()
    print(f"received: {node} {temperature} {brightness}")
