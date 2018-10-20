import time
import serial
import threading
from Utilities.NotificationCenter import NotificationCenter as NC

ser = None
sent = None


def receive():
    global sent

    while True:
        line = str(ser.readline())
        if line and line != sent:
            NC.default().post_notification('queue_broadcast',
                                           data=line, msg_id=None)


@NC.notify_on('broadcast')
def send(text):
    global sent
    sent = '~~{}||'.format(text)

    text = bytes(text.encode())
    ser.write(b"~~")
    ser.write(text)
    ser.write(b"||")


def start():
    serial.Serial(
        '/dev/ttyAMA0',
        baudrate=57600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    threading.Thread(target=receive).start()

