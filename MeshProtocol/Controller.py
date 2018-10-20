from Utilities.NotificationCenter import NotificationCenter as NC
from queue import Queue
from uuid import uuid4

data = {}

id_queue = Queue(maxsize=10)
@NC.notify_on('queue_broadcast')
def queue_broadcast(data, msg_id):

	if not msg_id:
		msg_id = str(uuid4())[1:5].upper()

	if msg_id in id_queue:
		return

	data[msg_id] = data
	id_queue.put(msg_id)
	NC.default().post_notification('broadcast', data=data,
								   msg_id=msg_id)