class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        if targetColor == color:
            return image

        rows = len(image)
        cols = len(image[0])

        q = deque([(sr, sc)])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                print(r, c)
                image[r][c] = color

                for dr, dc in directions:
                    nextR = r + dr
                    nextC = c + dc
                    if nextR >= 0 and nextC >= 0 and nextR < rows and nextC < cols and image[nextR][nextC] == targetColor:
                        q.append((nextR, nextC))

        return image