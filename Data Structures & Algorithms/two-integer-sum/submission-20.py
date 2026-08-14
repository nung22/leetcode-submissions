class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqs = {}

        for i,v in enumerate(nums):
            freqs[v] = freqs.get(v,[]) + [i]

            if target - v in nums[:i]:
                return [freqs[target - v].pop(0), freqs[v].pop(0)]

        return []

