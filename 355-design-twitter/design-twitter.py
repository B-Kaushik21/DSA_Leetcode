class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list) #[(time,tweetId)]
        self.following=defaultdict(set) # followerId-> set of followers

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=self.following[userId] | {userId}
        for u in users:
            for t in self.tweets[u][-10:]:
                heapq.heappush(heap,t)
        return [tweetid for _,tweetid in heapq.nlargest(10,heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)