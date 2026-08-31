from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = defaultdict(list)
        for i,num in enumerate(nums):
            num_map[num].append(i)
        for num in nums:
            if target - num in num_map.keys():
                if target - num != num:
                    return [num_map[num].pop(), num_map[target - num].pop()]
                elif target - num == num and len(num_map[num]) >= 2:
                    return num_map[num][:2]
                else:
                    continue

        return res