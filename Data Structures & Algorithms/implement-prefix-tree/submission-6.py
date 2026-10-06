class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.end_of_word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True
        
        