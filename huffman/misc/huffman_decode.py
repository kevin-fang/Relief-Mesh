from huffman import HuffmanCoding
import pickle

# location of sample text
path='./test.bin'

# load pregenerated huffman tree from file
with open('tree.bin', 'rb') as binary_file:
	f = binary_file.read()
	h = pickle.loads(f)


output_path = h.decompress(path)

print("Decompressed to {}".format(output_path))

