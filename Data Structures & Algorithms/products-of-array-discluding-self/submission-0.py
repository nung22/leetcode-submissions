class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:            
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        result = [product] * len(nums)            
        for i,v in enumerate(nums):
            if (v == 0 and zeros > 1) or (v != 0 and zeros > 0):
                result[i] = 0
            elif v != 0:
                result[i] //= v
        return result