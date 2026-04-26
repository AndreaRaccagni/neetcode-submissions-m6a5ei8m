class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            
            hashKey = tuple(count)

            if hashKey in anagramMap:
                anagramMap[hashKey].append(s)
            else:
                anagramMap[hashKey] = [s]

        return list(anagramMap.values())
    