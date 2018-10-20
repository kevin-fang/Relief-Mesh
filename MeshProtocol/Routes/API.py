from Utilities.NotificationCenter import NotificationCenter as NC
from flask import Blueprint, jsonify, request
from uuid import uuid4
from time import time

mod = Blueprint(__name__, 'api')
device_id = str(uuid4())[1:6].upper()


def _error(msg):
    return jsonify({
        "ok": False,
        "msg": msg
    })


@mod.route('/', methods=['GET'])
def index_get():
    return jsonify({
        "ok": True,
        "node": device_id,
        "time": time()
    })


msg_data = {}


@NC.notify_on('broadcast')
def broadcast_store(data, msg_id):
    msg_data[msg_id] = (data, time())


@mod.route('/history', methods=['GET'])
def history_get():

    data = list(msg_data.items())
    data.sort(key=lambda x: x[1][1])
    return jsonify({
        'ok': True,
        'data': [{'msg_id': msg_id,
                  'data': msg,
                  'timestamp': timestamp} for msg_id, (msg, timestamp) in data]
    })


@mod.route('/broadcast', methods=['POST'])
def broadcast_post():
    if not request.json:
        return _error('json required')
    if not 'data' in request.json:
        return _error('missing data')

    data = request.json['data']
    byte = bytes(data.encode())

    msg_id = str(uuid4())[1:5].upper()
    if 'msg_id' in request.json:
        msg_id = request.json['msg_id']

    if len(byte) > 250:
        return _error("data too large")

    NC.default().post_notification('queue_broadcast',
                                   threaded=False,
                                   data=data,
                                   msg_id=msg_id)
    return jsonify({
        "ok": True,
        "node": device_id,
        "bytes": len(byte),
        "data": data,
        "msg_id": msg_id
    })


@mod.route('/chat', methods=['GET'])
def chat_get():
    print(request.url_root[:-1])
    data = open('Routes/chat.html').read()
    return data.replace('$base_url', request.url_root[:-1])