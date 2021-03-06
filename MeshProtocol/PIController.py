import serial
import threading
from Utilities.NotificationCenter import NotificationCenter as NC

ser = None
sent = None
sent_nrf = None
ser_nrf = None


def strip(data):

    if not data:
        return None
    
    if type(data) == bytes():
        data = str(data.decode("utf-8"))
    if data[-1] == '\'':
        data = data[0:-1]
    return data.replace(r'||', '')\
               .replace(r'\r', '')\
               .replace(r'\n', '')\
               .replace(r'\r\n', '')\
               .replace(r'~~', '')\
               .replace('b\'', '')\
               .replace('b\"', '')\
               .strip()


def receive():
    global sent

    while True:
        line = str(ser.readline())
        if line and strip(line) != sent and line != "b''" and strip(line) != "":
            sent = strip(line)
            NC.default().post_notification('queue_broadcast',
                                           data=sent, msg_id=None)


def receive_nrf():
    global sent_nrf
    global ser_nrf

    while True:
        line = str(ser_nrf.readline())
        if line and strip(line) != sent_nrf and line != "b''" and strip(line) != "":
            sent = strip(line)
            NC.default().post_notification('queue_broadcast',
                                           data=sent, msg_id=None)
            NC.default().post_notification('queue_broadcast',
                                           data="G:42.429371,-88.607452", msg_id=None)


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
    ser.write(bytes(strip(data).encode()))
    ser.write(b"||")


def start():
    global ser

    try:
        ser = serial.Serial(
                '/dev/ttyACM0',
                baudrate=57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

        threading.Thread(target=receive).start()
    except Exception as err:
        print(err)


def start_nrf():
    global ser_nrf

    try:
        ser_nrf = serial.Serial(
            '/dev/ttyUSB0',
            baudrate=57600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        threading.Thread(target=receive_nrf).start()
    except Exception as err:
        print(err)
