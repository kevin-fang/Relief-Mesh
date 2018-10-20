from huffman import HuffmanCoding
import pickle

# sample input text
path='./sample_text.txt'

# load pregenerated huffman tree
with open('tree.bin', 'rb') as binary_file:
	f = binary_file.read()
	h = pickle.loads(f)

# compress tree
output_path = h.compress_file_with_predefined_tree(path)
print("Compressed output to: {}".format(output_path))