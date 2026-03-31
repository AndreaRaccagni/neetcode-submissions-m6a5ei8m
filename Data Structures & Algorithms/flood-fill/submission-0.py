class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        targetColor = image[sr][sc]

        if targetColor == color:
            return image

        def dfs(image, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != targetColor:
                return

            image[r][c] = color

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for moveRow, moveCol in directions:
                dfs(image, r + moveRow, c + moveCol)

        dfs(image, sr, sc)

        return image