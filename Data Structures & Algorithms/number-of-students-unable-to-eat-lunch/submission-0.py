class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsMap = {}

        for s in students:
            studentsMap[s] = studentsMap.get(s, 0) + 1

        studentsQueue = deque(students)
        sandwichesQueue = deque(sandwiches)

        while studentsQueue:
            curr = studentsQueue.popleft()

            if curr == sandwichesQueue[0]:
                sandwichesQueue.popleft()
                studentsMap[curr] -= 1
            else:
                studentsQueue.append(curr)
                if studentsMap[curr] == len(studentsQueue):
                    break

        return len(studentsQueue)

