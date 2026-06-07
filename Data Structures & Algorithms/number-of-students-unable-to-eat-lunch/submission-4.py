class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_counter = Counter(students)   

        for sandwich in sandwiches:
            if student_counter[sandwich] == 0:
                return student_counter[1 - sandwich]
            student_counter[sandwich] -= 1
        return 0