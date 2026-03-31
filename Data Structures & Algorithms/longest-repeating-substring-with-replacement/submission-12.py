class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charMap = [0] * 26
        mostFreq = 0
        maxWindow = 0
        
        for r in range(len(s)):    
            idx = ord(s[r]) - ord('A')
            charMap[idx] += 1
            mostFreq = max(mostFreq, charMap[idx])
            
            while r - l + 1 - mostFreq > k:
                charMap[ord(s[l]) - ord('A')] -= 1 
                l += 1
            
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow