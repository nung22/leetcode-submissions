class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(', ']':'[', '}':'{'}
        
        if len(s) % 2 != 0:
            return False

        res = []

        for p in s:
            if p in key:
                if not res or res.pop() != key[p]: 
                    return False
            else:
                res.append(p)
            
            print(res)


        return len(res) == 0