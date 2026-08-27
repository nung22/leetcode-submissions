class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s_freqs = defaultdict(int)
        for student in students:
            s_freqs[student] += 1
        
        for sandwich in sandwiches:
            if s_freqs[sandwich] == 0:
                return s_freqs[1] + s_freqs[0]
            s_freqs[sandwich] -= 1

        return 0