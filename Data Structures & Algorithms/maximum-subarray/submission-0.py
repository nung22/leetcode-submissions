class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        L = 0
        for R in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                L = R
            cur_sum += nums[R]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum

