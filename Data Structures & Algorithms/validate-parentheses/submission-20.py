class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(', ']':'[', '}':'{'}
        
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        res = []

        for p in s:
            if not res and p in key:
                return False
            if res and p in key and res[-1] == key[p]:
                res.pop()
            else:
                res.append(p)
            
            print(res)


        return len(res) == 0