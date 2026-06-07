class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_counter = Counter(students)
        q = deque(sandwiches)
        

        while q:
            sandwich = q[0]
            
            if student_counter[sandwich] == 0:
                student = 1 if sandwich == 0 else 0
                return student_counter[student]

            student_counter[sandwich] -= 1
            q.popleft()

        return 0