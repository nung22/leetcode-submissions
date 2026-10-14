class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(rate: int):
            time = 0
            for b in piles:
                time += math.ceil(b / rate)
            return time <= h
        
        largest_pile = max(piles)
        
        L, R = 1, largest_pile
        ans = largest_pile
        while L <= R:
            k = (R + L) // 2
            if canFinish(k):
                ans = k
                R = k - 1
            else:
                L = k + 1
        return ans