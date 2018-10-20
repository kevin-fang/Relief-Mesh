from app import socketio
from Utilities.NotificationCenter import NotificationCenter as NC

@NC.notify_on('broadcast')
def broadcast(data, device_id):
	socketio.emit('broadcast', data,
				  broadcast=True,
				  namespace='/mesh')

