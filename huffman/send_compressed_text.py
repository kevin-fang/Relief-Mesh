#!/usr/bin/env python3
import serial
import sys
import encode_text

ser = serial.Serial(
    '/dev/ttyACM1',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

def send(text):
    ser.write(b"~~")
    ser.write(text)
    ser.write(b"||")


if __name__ == "__main__":
    while True:
        text_to_send = input()
        encoded = encode_text.encode_text(str(len(text_to_send)) + "," + text_to_send)
        #print(encoded)
        send(encoded)
