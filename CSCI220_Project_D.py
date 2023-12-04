#CSCI 220 Final Project Group D 
#12-4-23

#class that holds the attributes for a node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq