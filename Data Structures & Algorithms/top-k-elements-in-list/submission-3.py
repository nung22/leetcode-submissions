import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        min_heap = []

        for num in nums:
            freqs[num] += 1

        for num in set(nums):
            heapq.heappush(min_heap, (freqs[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for _,num in min_heap]