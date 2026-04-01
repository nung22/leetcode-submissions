class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, 0
        d1, d2 = {}, {}
        letter = ''

        if len(s1) > len(s2): return False            
        

        while R < len(s2):
            if R - L < len(s1):
                if R < len(s1):
                    letter = s1[R]
                    d1[letter] = d1.get(letter, 0) + 1
                letter = s2[R]
                d2[letter] = d2.get(letter, 0) + 1
                R += 1

                if R < len(s1):
                    continue
            else:
                letter = s2[L]
                d2[letter] -= 1

                if d2[letter] == 0: 
                    del(d2[letter])

                L += 1
            print(d1, d2)
            if d1 == d2:
                return True

        return False