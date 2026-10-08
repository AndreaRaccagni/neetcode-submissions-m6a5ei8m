class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            index = len(self.tweets[followeeId]) - 1
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
        

        while minHeap and len(recentTweets) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            recentTweets.append(tweetId)

            if index >=0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
        
        self.followMap[userId].remove(userId)
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)    
