#!/usr/bin/env python3
from huffman import HuffmanCoding
import pickle

# generates a huffman tree from Pride and Prejudice corpus from Project Gutenberg: https://www.gutenberg.org/ebooks/1342
# https://www.gutenberg.org/files/1342/1342-0.txt
import urllib.request
corpus_url = "https://www.gutenberg.org/files/1342/1342-0.txt"

h = HuffmanCoding()

txt = urllib.request.urlopen(corpus_url).read().decode('utf-8')
#print(txt)
txt = txt.replace("“","\"")
txt = txt.replace("”","\"")
output_path = h.generate_tree(txt)

# save tree to file

tree_loc = "tree.bin"

with open(tree_loc, 'wb') as binary_file:
	pickle.dump(h, binary_file)

print("Tree generated at {}".format(tree_loc))
