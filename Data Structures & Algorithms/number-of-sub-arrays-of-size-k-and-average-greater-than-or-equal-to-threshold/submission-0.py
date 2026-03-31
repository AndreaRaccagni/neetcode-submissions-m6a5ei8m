class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[:k])

        if currSum / k >= threshold:
            count = 1

        for i in range(k, len(arr)):
            currSum += arr[i]
            currSum -= arr[i - k]
            count += 1 if currSum / k >= threshold else 0

        return count