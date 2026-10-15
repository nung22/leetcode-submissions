class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(list)
        for i,v in enumerate(nums):
            num_dict[v].append(i)
        for num in nums:
            i = num_dict[num].pop(0)
            remainder = target - num
            if remainder in num_dict and num_dict[remainder]:
                return [i, num_dict[target - num].pop()]