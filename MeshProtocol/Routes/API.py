from flask import Blueprint, jsonify
from uuid import uuid4
from time import time

mod = Blueprint(__name__, 'api')
device_id = str(uuid4())[1:6].upper()

@mod.route('/', methods=['GET'])
def index_get():
	return jsonify({
		"ok": True,
		"node": device_id,
		"time": time()
		})

