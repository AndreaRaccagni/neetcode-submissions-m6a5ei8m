class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            hashKey = self.hashWord(s)
            hashMap[hashKey].append(s)

        res = []
        for group in hashMap.values():
            res.append(group)

        return res

    def hashWord(self, word: str) -> str:
        count = [0] * 26

        for c in word:
            count[ord(c) - ord('a')] += 1
        
        for i in range(len(count)):
            count[i] = str(count[i])

        return '#'.join(count)