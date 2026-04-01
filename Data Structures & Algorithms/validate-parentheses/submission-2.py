class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if len(res) > 0 and ((i == "}" and res[-1] == "{") or (i == "]" and res[-1] == "[") or (i == ")" and res[-1] == "(")):
               res.pop()
            else:
                res.append(i)
        return len(res) == 0