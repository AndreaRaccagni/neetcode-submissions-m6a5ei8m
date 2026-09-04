class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        # build first window
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        # slide the window
        for i in range(k, len(nums)):
            left = i - k + 1
            while q and q[0] < left:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)
            res.append(nums[q[0]])

        return res