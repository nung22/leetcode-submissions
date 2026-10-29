class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track indices in dict with nums as keys
        num_dict = defaultdict(list)
        # iterate through nums
        for i,v in enumerate(nums):
            # calculate complement: target - num
            complement = target - v
            # if complement in dict return indices
            if complement in num_dict:
                return [num_dict[complement].pop(), i]
            # else add to dict
            else:
                num_dict[v].append(i)
        return []