class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapChar = {}
        for i in range(len(keyboard)):
            mapChar[keyboard[i]] = i

        total = mapChar[word[0]]
             
        for i in range(len(word) - 1):
            total += abs(mapChar[word[i]] - mapChar[word[i + 1]])

        return total