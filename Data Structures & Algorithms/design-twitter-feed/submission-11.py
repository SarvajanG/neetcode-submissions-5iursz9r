class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.followerIdTweets = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followerIdTweets[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        for followerId in self.followerIdTweets.keys():
            if userId != followerId and followerId not in self.followerMap[userId]:
                continue
            for tweet in self.followerIdTweets[followerId]:
                if len(minHeap) < 10:
                    heapq.heappush(minHeap, tweet)
                elif tweet > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, tweet)
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.followerMap[followerId]:
            return
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.followerMap[followerId]:
            return
        self.followerMap[followerId].remove(followeeId)
