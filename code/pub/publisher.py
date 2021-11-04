#!/usr/bin/python3

import zmq
import signal

from time import sleep
from random import randrange

#signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5555')

print('Publishing on *:5555')

while (True):
    # random data generation split into 10 publishing nodes
    node = randrange(1, 3)
    temperature = randrange(-20, 40)
    brightness = randrange(0, 100)

    print(f"sent: {node} {temperature} {brightness}")
    socket.send_string(f"{node} {temperature} {brightness}")
    sleep(1)
