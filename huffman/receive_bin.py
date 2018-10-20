import time
import serial
import huffman_decode_text

ser = serial.Serial(
    '/dev/ttyACM0',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def decode_input(huff):
    output = huffman_decode_text.decompress(huff[1:])
    length_re = r'(\d+),(.+)'
    import re
    searches = re.findall(length_re, output)[0]
    return searches[1][:int(searches[0])]

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
            print("should print now")
