import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k = [item[0] for item in counts.most_common(k)]

        return top_k