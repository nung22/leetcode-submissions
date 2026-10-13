class Solution:
    def compress(self, chars: List[str]) -> int:
        # initialize read and k ptrs
        # iterate through chars with read ptr
        n = len(chars)
        k = L = 0

        while L < n:
            chars[k] = chars[L]
            k += 1
            R = L + 1
            while R < n and chars[L] == chars[R]:
                R += 1
            
            if R - L > 1:
                for c in str(R - L):
                    chars[k] = c
                    k += 1
            L = R
        return k


