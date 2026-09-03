class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap = {}
        tMap = {}

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
 
        l = 0
        minLen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            
            while self.isSubstring(sMap, tMap):
                currWindow = r - l + 1
                if currWindow < minLen:
                    minLen = currWindow
                    res = [l, r]

                sMap[s[l]] -= 1
                l += 1


        if res[0] == -1:
            return ''

        return s[res[0] : res[1] + 1]


    def isSubstring(self, map1, map2):
        for k in map2:
            if k not in map1 or map1[k] < map2[k]:
                return False

        return True
