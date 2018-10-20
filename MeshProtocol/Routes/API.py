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

@mod.route('/broadcast', methods=['POST'])
def broadcast_post():

	if not request.json:
		return _error('json required')
	if not 'data' in request.json:
		return _error('missing data')

	data = request.json['data']
	byte = bytes(data.encode())

	if len(byte) > 250:
		return _error("data too large")

	NC.default().post_notification('broadcast',
 								   data=data,
 								   device_id=device_id)

	return jsonify({
		"ok": True,
		"node": device_id,
		"bytes": len(byte),
		"data": data
		})
