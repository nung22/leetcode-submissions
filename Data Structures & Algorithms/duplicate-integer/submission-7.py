class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num in vals.keys():
                return True
            vals[num] = 1
        
        return False