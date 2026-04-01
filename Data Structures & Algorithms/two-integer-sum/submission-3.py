class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i,v in enumerate(nums):
            numDict[v] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDict and numDict[complement] != i:
                return [i, numDict[complement]]

        return 0 