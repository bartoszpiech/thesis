import time
import requests

IP = 'http://192.168.0.164:5000'


for i in range(100):
    r = requests.get(IP + '/api/open/' + str(i))
    print('Opened ' + str(i) + ' node, response: ' + str(r.text))
    #time.sleep(1)
