class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        tracker = 0

        while True:
            print(students, sandwiches)
            if tracker == len(students):
                break

            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                tracker += 1
                continue
            
            students.pop(0)
            sandwiches.pop(0)
            tracker = 0

        return tracker