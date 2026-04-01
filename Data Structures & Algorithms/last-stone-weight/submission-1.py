class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest, nextHeaviest = stones[len(stones) - 1], stones[len(stones) - 2]
            if heaviest == nextHeaviest:
                stones.pop(len(stones) - 1)
            else:
                stones[len(stones) - 2] = heaviest - nextHeaviest
            if len(stones) == 0:
                return 0
            else: 
                stones.pop(len(stones) - 1)
        
        if len(stones) == 0:
            return 0
        return stones[0]



