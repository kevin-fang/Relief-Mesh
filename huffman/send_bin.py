import serial
import sys

with open(sys.argv[1], 'rb') as file:
	for i in file:
		print(i)