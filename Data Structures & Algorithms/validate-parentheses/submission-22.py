class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(', ']':'[', '}':'{'}
        
        if len(s) % 2 != 0:
            return False

        res = []

        for p in s:
            if p in key:
                if not res:
                    return False
                else:
                    if res[-1] == key[p]:
                        res.pop()
                    else:
                        return False
            else:
                res.append(p)
            
            print(res)


        return len(res) == 0