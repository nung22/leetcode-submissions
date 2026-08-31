from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                # Pair found! The previous index is seen[complement]
                return [seen[complement], i]
            seen[val] = i