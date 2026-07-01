class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d, res = {}, []

        for i,v in enumerate(nums):
            d[v] = d.get(v, [])
            d[v].append(i)
        print(d)
        for i,v in enumerate(nums):
            if target - v in d:
                if target - v == v:
                    if len(d[v]) < 2:
                        continue
                    res =  [i, d[v][1]]
                else:
                    res = [i, d[target - v][0]]
                break
        
        return res