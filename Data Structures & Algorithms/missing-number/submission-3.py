class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in sorted(nums):
            if num != res:
                break
            res += 1
        return res