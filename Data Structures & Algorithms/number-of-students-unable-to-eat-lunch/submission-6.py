from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungry_students = Counter(students)
        while sandwiches and hungry_students[sandwiches[0]] > 0:
            hungry_students[sandwiches[0]] -= 1
            sandwiches.pop(0)
        return hungry_students[0] + hungry_students[1]