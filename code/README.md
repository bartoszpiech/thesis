# IoT server using Blockchain technology
I implemented an Internet of Things server using Blockchain technology. It's
written in Python with Flask web framework for server and ZeroMQ module for
node communication.

## Quick start
You have to install those packages:
- Python3 (`$ sudo apt install python3` || `$ sudo pacman -S python3`),
- Python3 libraries (`$ pip install -r requirements.txt`),

### Server
To run server, you'll have to:
- change run\_server.sh script accordingly to your device specs (IP address etc.),
- run server using `$ ./run_server`

### Nodes
You can run "server nodes"/"responders" that communicate with the blockchain itself and "client nodes"/"requesters" that try to communicate with "server nodes".
You can run server node using `$ python responder.py`
You can run client node using `$ python requester.py`
