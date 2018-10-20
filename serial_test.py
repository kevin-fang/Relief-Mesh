import time
import serial

ser = serial.Serial(
    '/dev/ttyAMA0',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
while 1:
    line = ser.readline()
    print(line)