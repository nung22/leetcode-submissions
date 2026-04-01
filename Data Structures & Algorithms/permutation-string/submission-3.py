class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, 0
        d1, d2 = {}, {}
        letter = ''

        if len(s1) > len(s1): return False

        for c in s1:
            d1[c] = d1.get(c, 0) + 1
        

        while R < len(s2):
            if R - L == len(s1):
                letter = s2[L]
                d2[letter] -= 1

                if d2[letter] == 0: 
                    del(d2[letter])

                L += 1
            else:
                letter = s2[R]
                d2[letter] = d2.get(letter, 0) + 1
                R += 1
            print(d1, d2)
            if d1 == d2:
                return True

        return False