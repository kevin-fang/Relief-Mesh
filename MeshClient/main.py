from socketIO_client import SocketIO, BaseNamespace
import requests
import json
from threading import Thread

class Streamer(BaseNamespace):
    def on_connect(self):
        print('Streamer: connected')

    def on_disconnect(self):
        print('Streamer: disconnected')

    def on_broadcast(self, data):
        print('{}: {}'.format(data['msg_id'], data['data']))

host, port = '0.0.0.0', 8080
def run_socket():
	socket = SocketIO(host, port)
	stream_namespace = socket.define(Streamer, '/mesh')
	socket.wait()

Thread(target=run_socket).start()

while True:
	data = input()
	requests.post('http://{}:{}/broadcast'.format(host, port),
				  json={'data': data})

