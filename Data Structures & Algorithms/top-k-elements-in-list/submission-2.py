import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        max_pq = []
        res = []

        for num in nums:
            freqs[num] += 1

        for num in set(nums):
            heapq.heappush(max_pq, (-freqs[num], num))

        for _ in range(k):
            _, n = heapq.heappop(max_pq)
            res.append(n)

        return res