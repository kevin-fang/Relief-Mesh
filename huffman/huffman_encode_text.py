from huffman import HuffmanCoding
import pickle
import sys

try: 
	# load pregenerated huffman tree
	with open('tree.bin', 'rb') as binary_file:
		f = binary_file.read()
		h = pickle.loads(f)

	print("Successfully loaded input tree.")
except FileNotFoundError:
	print("tree.bin not found. Please run `python generate_tree.py`")
	sys.exit(1)

def encode_text(text):
	output_text = h.compress_input_with_predefined_tree(text)
	return output_text

if __name__ == "__main__":
	for item in sys.argv[1:]:
		print(h.compress_input_with_predefined_tree(item))