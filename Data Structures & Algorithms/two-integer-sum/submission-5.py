class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]].append(i)
            else:
                numDict[nums[i]] = [i]
        
        print(numDict)

        for num in nums:
            res.append(numDict[num].pop(0))
            diff = target - num
            if diff in numDict and len(numDict[diff]) > 0:
                res.append(numDict[diff].pop(0))
                return res
            res.pop(0)


