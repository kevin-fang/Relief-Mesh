from Utilities.NotificationCenter import NotificationCenter as NC
from uuid import uuid4
import re
from threading import Thread
from socketIO_client import SocketIO, BaseNamespace
import requests
import logging

id_queue = list()
server = False


class Streamer(BaseNamespace):

    def on_connect(self):
        print('Streamer: connected')

    def on_disconnect(self):
        print('Streamer: disconnected')

    def on_broadcast(self, data):
        NC.default().post_notification('queue_broadcast',
                                       threaded=True,
                                       data=data['data'],
                                       msg_id=data['msg_id'])


def run_socket():
    logging.getLogger('socketIO-client').setLevel(logging.CRITICAL)
    host, port = 'api.pillup.org', 80
    socket = SocketIO(host, port)
    stream_namespace = socket.define(Streamer, '/mesh')
    socket.wait()


def start_streamer():
    Thread(target=run_socket).start()


@NC.notify_on('queue_broadcast')
def queue_broadcast(data, msg_id=None):

    myre = re.compile('^(.{4}):.*$')
    if myre.match(data):
        msg_id = myre.findall(data)
        data = data[5:]

    if not msg_id:
        msg_id = str(uuid4())[1:5].upper()

    if msg_id in id_queue:
        return

    id_queue.append(msg_id)
    NC.default().post_notification('broadcast', data=data,
                                   msg_id=msg_id)


@NC.notify_on('broadcast')
def broadcast_to_server(data, msg_id):

    if server:
        return

    try:
        data = {'data': data, 'msg_id': msg_id}
        print(requests.post('http://api.pillup.org/broadcast', json=data).content)
    except Exception as err:
        print(err)