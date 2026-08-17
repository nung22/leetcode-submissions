import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        min_heap = []

        for num in set(nums):
            heapq.heappush(min_heap, (freqs[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for _,num in min_heap]