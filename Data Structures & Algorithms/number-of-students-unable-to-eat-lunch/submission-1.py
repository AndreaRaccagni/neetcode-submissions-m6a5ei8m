class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        eats = 0
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                eats += 1
                count[s] -= 1
            else:
                break

        return len(students) - eats

