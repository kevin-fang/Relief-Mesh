from huffman import HuffmanCoding
import pickle

# generates a huffman tree from Pride and Prejudice corpus from Project Gutenberg: https://www.gutenberg.org/ebooks/1342

path='./pride_and_prejudice.txt'

h = HuffmanCoding(path)

output_path = h.generate_tree()

# save tree to file

tree_loc = "tree.bin"

with open(tree_loc, 'wb') as binary_file:
	pickle.dump(h, binary_file)

print("Tree generated at {}".format(tree_loc))