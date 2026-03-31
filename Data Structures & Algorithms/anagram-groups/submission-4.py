class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped_anagrams = {}

        for string in strs:
            str_map = [0] * 26
            for char in string:
                str_map[ord(char) - ord('a')] += 1

            hash_str = ''
            for num in str_map:
                hash_str += str(num) + '*'
            
            if hash_str in mapped_anagrams:
                mapped_anagrams[hash_str].append(string)
            else:
                mapped_anagrams[hash_str] = [string]
            
            print()
            print(mapped_anagrams)

        return list(mapped_anagrams.values())



    