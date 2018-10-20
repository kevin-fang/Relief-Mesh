from Utilities.NotificationCenter import NotificationCenter as NC
from uuid import uuid4
import re

id_queue = list()


@NC.notify_on('queue_broadcast')
def queue_broadcast(data, msg_id):

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
