class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappedAnagrams = defaultdict(list)

        for s in strs:
            key = self.generateHash(s)
            mappedAnagrams[key].append(s)

        return list(mappedAnagrams.values())



    def generateHash(self, s: str) -> str:
        count = [0] * 26
        shift = ord('a')

        for c in s:
            count[ord(c) - shift] += 1
        
        res = ''
        for c in count:
            res += '#' + str(c)

        return res