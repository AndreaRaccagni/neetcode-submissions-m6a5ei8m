class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        tuplePoint = tuple(point)
        self.points[tuplePoint] = self.points.get(tuplePoint, 0) + 1

    def count(self, point: List[int]) -> int:
        total = 0

        for p in self.points:
            if p[0] == point[0] and p != point:
                distance = abs(p[1] - point[1])
                if distance == 0:
                    continue

                if (p[0] + distance, p[1]) in self.points and (point[0] + distance, point[1]) in self.points:
                    total += self.points[(p[0] + distance, p[1])] * self.points[(point[0] + distance, point[1])] * self.points[(p[0], p[1])]
                if (p[0] - distance, p[1]) in self.points and (point[0] - distance, point[1]) in self.points:
                    total += self.points[(p[0] - distance, p[1])] * self.points[(point[0] - distance, point[1])] * self.points[(p[0], p[1])]
        
        return total
