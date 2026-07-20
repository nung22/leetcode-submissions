class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        total_sum = 0

        for o in operations:
            temp = 0

            if o == '+':
                temp = scores[-1] + scores[-2]
            elif o == 'D':
                temp = scores[-1] * 2
            elif o == 'C':
                total_sum -= scores.pop()
                continue
            else:
                temp = int(o)
            
            scores.append(temp)
            total_sum += temp
        
        return total_sum