class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list) # userId: [(tweetId, timestamp)]
        self.userFollows = defaultdict(set) # userId: [userId]
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1
        if len(self.userTweets[userId]) > 10:
            self.userTweets[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        userFollows = self.userFollows[userId]
        userFollows.add(userId)
        heap = []
        for user in userFollows:
            tweets = self.userTweets[user]
            for tweet in tweets:
                heapq.heappush(heap, tweet)

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        
