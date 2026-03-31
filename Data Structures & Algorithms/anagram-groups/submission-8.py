class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            counter = [0] * 26

            for c in str:
                index = ord(c) - ord('a')
                counter[index] += 1

            wordHash = ''
            for c in counter:
                wordHash += f"{c}#"

            if wordHash in res:
                res[wordHash].append(str)
            else:
                res[wordHash] = [str]
        
        return list(res.values())


