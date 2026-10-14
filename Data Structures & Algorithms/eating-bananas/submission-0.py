class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def guessEating(rate: int):
            time = 0
            for b in piles:
                time += (b + rate - 1) // rate
            return time <= h
        
        largest_pile = 0
        for p in piles:
            largest_pile = max(largest_pile, p)
        
        L, R = 1, largest_pile
        ans = largest_pile
        while L <= R:
            k = (R + L) // 2
            if guessEating(k):
                ans = k
                R = k - 1
            else:
                L = k + 1
        return ans