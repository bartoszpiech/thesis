#!/usr/bin/python3

import zmq
import signal

from time import sleep

signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5555')

while (True):
    socket.send(b'status 5')
    socket.send(b'all is well')
    sleep(1)
