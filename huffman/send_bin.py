import serial
import sys

ser = serial.Serial(
    '/dev/ttyACM0',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
with open(sys.argv[1], 'rb') as file:
    for i in file:
        ser.write("~~")
        ser.write(i)
        ser.write("||")
