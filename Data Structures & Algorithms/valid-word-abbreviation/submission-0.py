class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == '0':
                return False
            
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else:
                num_window = ''
                while j < len(abbr) and abbr[j].isdigit():
                    num_window += abbr[j]
                    j += 1
                
                shift = int(num_window)
                i += shift

        return i == len(word) and j == len(abbr)
