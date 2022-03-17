class TrieNode:            
            
        def __init__(self, is_end = False):
            self.is_end = is_end
            self.links = [None] * 26
            
        def containKey(self, char):
            return self.links[ord(char) - ord('a')] != None
        
        def isEnd(self):
            return self.is_end
        
        def setEnd(self):
            self.is_end = True
        
        def put(self, node, char):
            self.links[ord(char) - ord('a')] = node
        
        def get(self, char):
            return self.links[ord(char) - ord('a')]
    
class Trie:
    
     
        
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.containKey(c):
                node.put(TrieNode(), c)
            node = node.get(c)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.containKey(c):
                return False
            node = node.get(c)
        
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.containKey(c):
                return False
            node = node.get(c)
        
        return True
