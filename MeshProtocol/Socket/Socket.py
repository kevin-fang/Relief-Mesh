from app import socketio
from Utilities.NotificationCenter import NotificationCenter as NC


@NC.notify_on('broadcast')
def broadcast(data, msg_id):
    data = {'data': data, 'msg_id': msg_id}
    print('data', data)
    socketio.emit('broadcast', data,
                  broadcast=True,
                  namespace='/mesh')


@socketio.on('data', namespace='/mesh')
def handle_data(data):
    NC.default().post_notification('queue_broadcast',
                                   data=data,
                                   msg_id=None)

@socketio.on('ping', namespace='/mesh')
def handle_ping(data):
    socketio.emit('pong', 'pong')