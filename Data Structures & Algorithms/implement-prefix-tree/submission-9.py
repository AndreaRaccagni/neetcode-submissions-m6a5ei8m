class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()   
            curr = curr.children[index]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False 
            curr = curr.children[index]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False 
            curr = curr.children[index]
        return True
        