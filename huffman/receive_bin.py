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

compr_builder = b''
try:
    while 1:
        line = ser.readline()
        if (line != b''):
            print("Received message")
            #print(line[:-4])
            if line[0] == ord("~"):
                print("start")
                compr_builder += line[1:]
            else:
                print(line)
                compr_builder += line
        #while line[-1] != "|":
        #    compr_builder += line
        #    line = ser.readline()
        #print(huffman_decode_text.decompress(line))
except KeyboardInterrupt:
    if compr_builder != b'':
        #print(compr_builder)
        print()
        output = huffman_decode_text.decompress(compr_builder[1:])
        length_re = r'(\d+),(.+)'
        import re
        searches = re.findall(length_re, output)[0]
        print(searches[1][:int(searches[0])])
