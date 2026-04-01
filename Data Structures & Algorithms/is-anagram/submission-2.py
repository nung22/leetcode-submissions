class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            letters[l] = letters.get(l, 0) + 1
        
        for l in t:
            if not letters.get(l):
                return False
            letters[l] = letters.get(l) - 1
            if letters[l] == 0:
                letters.pop(l)

        return len(letters) == 0