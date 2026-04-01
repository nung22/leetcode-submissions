class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fullSum, partialSum, i = 0, 0, 0
        
        for num in nums:
            partialSum += num
            fullSum += i
            i += 1
        
        return fullSum + i - partialSum
