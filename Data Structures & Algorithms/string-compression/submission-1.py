class Solution:
    def compress(self, chars: List[str]) -> int:
        # variables: k, length of chars, left ptr
        n = len(chars)
        k = L = 0
        # iterate through chars with left ptr
        while L < n:
            # write to compressed str - s
            chars[k] = chars[L]
            # increment k
            k += 1
            # initialize right ptr
            R = L + 1
            # while right and left are equal increment right
            while R < n and chars[R] == chars[L]:
                R += 1
            # write the length of the sequence to s if greater than 1
            if R - L > 1:
                for c in str(R - L):
                    chars[k] = c
                    k += 1
            # set left to right
            L = R
        return k
