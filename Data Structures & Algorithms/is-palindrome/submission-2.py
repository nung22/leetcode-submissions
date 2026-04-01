class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        lst = s.replace(" ","").lower()
        L, R = 0, len(lst) - 1
        while L < R:
            if not lst[L].isalnum():
                L += 1
                continue
            if not lst[R].isalnum():
                R -= 1
                continue
            if lst[L] != lst[R]:
                return False
            else:
                L += 1
                R -= 1
        return True