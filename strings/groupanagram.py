from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

# Read input
strs = input().split()  # List of strings

solution = Solution()
result = solution.groupAnagrams(strs)
print(result)
