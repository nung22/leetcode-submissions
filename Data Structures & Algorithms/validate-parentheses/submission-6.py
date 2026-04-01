class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        res = len(s) / 2

        for p in s:
            if p in pMap.values():
                stack.append(p)
                continue
            if len(stack) > 0 and pMap[p] == stack[-1]:
                stack.pop()
                res -= 1
        return res == 0
