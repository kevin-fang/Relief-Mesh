import time
import serial
import threading
from Utilities.NotificationCenter import NotificationCenter as NC

ser = None
sent = None


def strip(data):

    if type(data) == bytes():
        data = data.decode("utf-8")
    return data.replace('||', '')\
               .replace('~~', '')\
               .strip()


def receive():
    global sent

    while True:
        line = str(ser.readline())
        if line and strip(line) != strip(sent) and line != "b''":
            sent = strip(line)

            NC.default().post_notification('queue_broadcast',
                                           data=line, msg_id=None)


@NC.notify_on('broadcast')
def send(data, msg_id=None):
    global sent
    global ser

    if not ser:
        return

    if sent == strip(data):
        return
    sent = strip(data)

    ser.write(b"~~")
    ser.write(strip(data))
    ser.write(b"||")


def start():
    global ser

    ser = serial.Serial(
            '/dev/ttyACM1',
            baudrate=57600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    threading.Thread(target=receive).start()

