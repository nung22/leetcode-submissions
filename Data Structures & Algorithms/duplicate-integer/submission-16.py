class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        num_set = set(nums)
        return len(num_set) != len(nums)