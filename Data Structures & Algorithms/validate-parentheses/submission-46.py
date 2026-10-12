class Solution:
    def isValid(self, s: str) -> bool:
        key = {'}':'{', ')':'(', ']':'['}
        stack = []
        for paren in s:
            if paren in key:
                if not stack or stack[-1] != key[paren]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(paren)
        return not stack