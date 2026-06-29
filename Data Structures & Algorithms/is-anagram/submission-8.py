class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ft = {}

        for char in s:
            ft[char] = ft.get(char, 0) + 1
        
        for char in t:
            if char not in ft or ft[char] == 0:
                return False
            if char in ft:
                ft[char] -= 1

        return True