class Twitter:
    import heapq
    from collections import defaultdict

    def __init__(self):
        # userId -> unique set of followers   (UserID)
        # userId -> stack of user's post with (count, TweetID)
        self.count = 0
        self.followerMap = defaultdict(set) # userId: userId          # people he is following
        self.userPosts = defaultdict(list) # userId: (count, TweetID) # where count is used to sort

    def postTweet(self, userId: int, tweetId: int) -> None:
        # for all followers of userId, 
        self.userPosts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = []

        self.followerMap[userId].add(userId)
        for follow_id in self.followerMap[userId]:
            if follow_id in self.userPosts:
                idx = len(self.userPosts[follow_id]) - 1
                count, tweet_id = self.userPosts[follow_id][idx]
                heapq.heappush(minHeap, (count, tweet_id, idx - 1, follow_id))

        while minHeap and len(result) < 10:
            count, tweet_id, idx, follow_id = heapq.heappop(minHeap)
            result.append(tweet_id)
            if idx >= 0:
                count, tweet_id = self.userPosts[follow_id][idx]
                heapq.heappush(minHeap, (count, tweet_id, idx - 1, follow_id))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
