class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            prev = flowerbed[i - 1] if i > 0 else 0
            curr = flowerbed[i]
            nxt = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0

            if prev == 0 and curr == 0 and nxt == 0:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True

        return count >= n