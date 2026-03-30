class Node:
    ORD_a = ord('a')
    ORD_z = ord('z')
    ORD_A = ord('A')
    ORD_Z = ord('Z')

    @staticmethod
    def convert_index(c):
        if ord(c) >= Node.ORD_a and ord(c) <= Node.ORD_z:
            return ord(c) - Node.ORD_a
        
        return 26 + ord(c) - Node.ORD_A

    def __init__(self):
        self.ends = False
        self.children = [None]*52
    
    def add_chr(self, c):
        idx = Node.convert_index(c)
        if self.children[idx] is None:
            self.children[idx] = Node()
        
        return self.children[idx]
    
    def get_next(self, c):
        idx = Node.convert_index(c)
        return self.children[idx]

    def end(self):
        self.ends = True
    
    def is_end(self):
        return self.ends == True

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        st = self.root
        for c in word:
            st = st.add_chr(c)
        st.end()

    def search_helper(self, word):
        st = self.root
        for c in word:
            st = st.get_next(c)
            if st is None:
                break
        
        return st

    def search(self, word: str) -> bool:
        node = self.search_helper(word)
        return node is not None and node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.search_helper(prefix)
        return node is not None

"""
root -> [0..25] points to other nodes

Node:
    end = False
    children: [0]*52
    Fn index(Chr) -> appropriate location

root = Node()
start = root
for c in word:
    idx = index(c)
    start.children[idx] = Node()
    start = start.children[idx]
start.end = True

"""