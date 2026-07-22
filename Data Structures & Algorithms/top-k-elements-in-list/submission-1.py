class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        print(freqs)
        sorted_keys = sorted(freqs, key=freqs.get, reverse=True)
        return sorted_keys[:k]