from huffman import HuffmanCoding

path='./sample_text.txt'

h = HuffmanCoding(path)

output_path = h.compress()
print(output_path)
print(h.decompress(output_path))

