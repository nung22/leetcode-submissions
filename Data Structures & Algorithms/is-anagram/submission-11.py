from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs = defaultdict(int)

        for char in s:
            freqs[char] += 1
        
        for char in t:
            if freqs[char] == 0:
                return False
            freqs[char] -= 1
        
        return True