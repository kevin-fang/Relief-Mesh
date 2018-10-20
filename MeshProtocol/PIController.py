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
        if line and line != sent and line != "b''":
            print(line)
            sent = line
            #NC.default().post_notification('queue_broadcast',
             #                              data=line, msg_id=None)


@NC.notify_on('broadcast')
def send(data, msg_id=None):
    global sent
    global ser

    if not ser:
        return
    text = data
    temp = str(bytes('~~{}||\r\n'.format(text).encode()))
    if temp == sent:
        return
    sent = temp
    print('sending {}'.format(sent))
    text = bytes(text.encode())
    ser.write(b"~~")
    ser.write(text)
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

