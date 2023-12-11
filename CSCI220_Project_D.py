#CSCI 220 Final Project Group D 
#12-4-23

#class that holds the attributes for a node
# A Huffman Tree Node 
import heapq 
  
  
class node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        # frequency of symbol 
        self.freq = freq 
  
        # symbol name (character) 
        self.symbol = symbol 
  
        # node left of current node 
        self.left = left 
  
        # node right of current node 
        self.right = right 
  
        # tree direction (0/1) 
        self.huff = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq
    
    #Decode function
    def decode_huffman(encoded_str, root):
        decoded_str = ''
        current_node = root

        for bit in encoded_str:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if not current_node.left and not current_node.right:
                decoded_str += current_node.symbol
                current_node = root  # Reset to the root for the next character
        return decoded_str
    
    #Encode function
    def encode_huffman(char, root, current=''):
        if not root:
            return None
        if root.symbol == char:
            return current
        left_encode = node.encode_huffman(char, root.left, current + '0')
        right_encode = node.encode_huffman(char, root.right, current + '1')
        return left_encode if left_encode is not None else right_encode
    
#Read data from a text file
def read_data_from_file(filename):
    chars = []
    freq = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            chars.append(data[0])
            freq.append(float(data[1]))
    return chars, freq

def main():
    filename = 'dataTeamX.txt'

    # Read data from the file
    chars, freq = read_data_from_file(filename)
  
    # utility function to print huffman 
    # codes for all symbols in the newly 
    # created Huffman tree 
    def printNodes(node, val=''): 
    
        # huffman code for current node 
        newVal = val + str(node.huff) 
    
        # if node is not an edge node 
        # then traverse inside it 
        if(node.left): 
            printNodes(node.left, newVal) 
        if(node.right): 
            printNodes(node.right, newVal) 
    
            # if node is edge node then 
            # display its huffman code 
        if(not node.left and not node.right): 
            print(f"{node.symbol} -> {newVal}") 
    
    # list containing unused nodes 
    nodes = [] 
    
    # converting characters and frequencies 
    # into huffman tree nodes 
    for x in range(len(chars)): 
        heapq.heappush(nodes, node(freq[x], chars[x])) 
    
    while len(nodes) > 1: 
    
        # sort all the nodes in ascending order 
        # based on their frequency 
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes) 
    
        # assign directional value to these nodes 
        left.huff = 0
        right.huff = 1
    
        # combine the 2 smallest nodes to create 
        # new node as their parent 
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 
    
        heapq.heappush(nodes, newNode) 
    
    # Huffman Tree is ready! 
    huffman_root = nodes[0]
    printNodes(huffman_root)

    #assigns the encoded and decoded strings to variables
    encoded_str = ' '.join([node.encode_huffman(char, huffman_root) for char in chars])
    decoded_str = node.decode_huffman(encoded_str, huffman_root)

    #prints the original strings and frequencies; encoded strings; decoded strings
    print(f"Original String and respective frequency: {chars}, {freq}")
    print(f"Encoded String: {encoded_str}")
    print(f"Decoded String: {decoded_str}")

if __name__ == "__main__":
    main()