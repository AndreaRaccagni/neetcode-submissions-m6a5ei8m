class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += -1
        self.tweets[userId].append((tweetId, self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        recentTweets = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            index = len(self.tweets[followeeId]) - 1
            if index >= 0:
                tweetId, count = self.tweets[followeeId][index]
                heapq.heappush(minHeap, (count, followeeId, tweetId, index - 1))

        while minHeap and len(recentTweets) < 10:
            count, followeeId, tweetId, currIndex = heapq.heappop(minHeap)
            recentTweets.append(tweetId)

            if currIndex >= 0:
                tweetId, count = self.tweets[followeeId][currIndex] 
                heapq.heappush(minHeap, (count, followeeId, tweetId, currIndex - 1))
        
        self.followMap[userId].remove(userId)
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
