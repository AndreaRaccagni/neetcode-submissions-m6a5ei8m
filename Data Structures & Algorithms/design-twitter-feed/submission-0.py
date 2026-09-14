class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                last = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][last]
                heapq.heappush(minHeap, [count, tweetId, followeeId, last - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, last = heapq.heappop(minHeap)
            res.append(tweetId)
            if last >= 0:
                count, tweetId = self.tweets[followeeId][last]
                heapq.heappush(minHeap, [count, tweetId, followeeId, last - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
