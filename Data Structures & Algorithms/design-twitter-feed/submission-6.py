class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweets = {}
        self.count = 0
        self.feedsLen = 10


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        recentTweets = []

        followees = self.followMap.get(userId, set())
        followees.add(userId)

        for followeeId in followees:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, (count, followeeId, tweetId, index - 1))

        while maxHeap and len(recentTweets) < self.feedsLen:
            if maxHeap:
                count, followeeId, tweetId, index = heapq.heappop(maxHeap)
                recentTweets.append(tweetId)
            if index >= 0:
                lastCount, lastTweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, (lastCount, followeeId, lastTweetId, index - 1))

        return recentTweets

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followMap.get(followerId):
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followMap.get(followerId)
        if followees and followeeId in followees :
            self.followMap[followerId].remove(followeeId)
        
