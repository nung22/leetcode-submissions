# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # pick range from 1 to n
        L, R = 1, n
        res = 0
        # iterate while L less than R 
        while L <= R:
            # pick midpoint
            mid = (R + L) // 2
            # adjust pointers based on guess() response
            if guess(mid) == -1:
                R = mid - 1
            elif guess(mid) == 1:
                L = mid + 1
            else:
                return mid
