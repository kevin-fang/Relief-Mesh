#!/usr/bin/env python3
import time
import serial
import decode_text

ser = serial.Serial(
    '/dev/ttyACM1',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def decode_input(huff):
    output = decode_text.decompress(huff[1:])
    length_re = r'(\d+),(.+)'
    import re
    searches = re.findall(length_re, output)[0]
    if searches != None:
        return searches[1][:int(searches[0])]
    else:
        return None

compr_builder = b''
while 1:
    line = ser.readline()
    if (line != b''):
        if line[0] == ord("~"):
            compr_builder += line[1:]
            if line[-1] == ord('\n'):
                print(decode_input(compr_builder))
                compr_builder = b''
        elif line[-1] != ord("\n"):
            print(line)
            compr_builder += line
        else:
            print(decode_input(compr_builder))
