class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        tuplePoint = tuple(point)
        self.points[tuplePoint] = self.points.get(tuplePoint, 0) + 1

    def count(self, point: List[int]) -> int:
        total = 0
        for a in self.points:
            if a[0] == point[0] and a != point:
                distance = abs(a[1] - point[1])
                if distance == 0:
                    continue

                if (a[0] + distance, a[1]) in self.points and (point[0] + distance, point[1]) in self.points:
                    total += self.points[(a[0] + distance, a[1])] * self.points[(point[0] + distance, point[1])] * self.points[(a[0], a[1])]
                if (a[0] - distance, a[1]) in self.points and (point[0] - distance, point[1]) in self.points:
                    total += self.points[(a[0] - distance, a[1])] * self.points[(point[0] - distance, point[1])] * self.points[(a[0], a[1])]
                
        return total
