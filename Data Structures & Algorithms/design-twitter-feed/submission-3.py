class Twitter:

    def __init__(self):
        self.tweets = []
        self.feed = []
        self.followerFollowee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([len(self.tweets), userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.feed = []
        for tweet in self.tweets:
            if tweet[1] == userId or tweet[1] in self.followerFollowee[userId]:
                self.feed.append(tweet)
        self.feed.sort(reverse=True)
        self.feed = [i[2] for i in self.feed[:10]]
        print(self.feed)
        return self.feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerFollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerFollowee[followerId]:
            self.followerFollowee[followerId].remove(followeeId)
