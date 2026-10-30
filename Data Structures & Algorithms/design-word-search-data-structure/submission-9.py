class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in curr.children:
                        if child and dfs(j + 1, child):
                            return True
                    return False 
                else:
                    index = ord(c) - ord('a')
                    if not curr.children[index]:
                        return False
                    curr = curr.children[index]
            return curr.end

        return dfs(0, self.root)