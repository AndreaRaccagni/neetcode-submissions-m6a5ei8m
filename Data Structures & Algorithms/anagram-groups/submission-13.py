class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            counter = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                counter[index] += 1
        
            key = tuple(counter)
            if key not in res:
                res[key] = []

            res[key].append(s)

        return list(res.values())