#!/usr/bin/env python3
from huffman import HuffmanCoding
import pickle

# location of sample text
path='./sample_text.bin'

# load pregenerated huffman tree from file
with open('tree.bin', 'rb') as binary_file:
	f = binary_file.read()
	h = pickle.loads(f)

def decompress(input_text):
    output_text = h.decompress_from_text(input_text)
    return output_text

if __name__ == "__main__":
    while True:
        input_text = input()
    	output_text = h.decompress_from_text(input_text)
    	print(output_text)
