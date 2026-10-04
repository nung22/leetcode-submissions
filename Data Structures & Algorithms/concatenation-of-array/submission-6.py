class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums) * 2

        for i, v in enumerate(nums):
            res[i] = res[(len(res) // 2) + i] = v
        
        return res