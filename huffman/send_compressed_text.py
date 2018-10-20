import serial
import sys
import huffman_encode_text

ser = serial.Serial(
    '/dev/ttyACM0',
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
    text_to_send = input()
    encoded = huffman_encode_text.encode_text(str(len(text_to_send)) + "," + text_to_send)
    print(encoded)
    send(encoded)
