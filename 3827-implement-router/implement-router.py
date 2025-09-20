class Router:

    def __init__(self, memoryLimit: int):
        self.maxSize=memoryLimit
        self.mpp={}
        self.st={}
        self.timestamps={}
        self.queue=deque()
    
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet=(source,destination,timestamp)
        if packet in self.mpp:
            return False
        if len(self.queue)==self.maxSize:
            res=self.queue.popleft()
            del self.mpp[res]
            temp=res[1]
            self.st[temp]=self.st.get(temp,0)+1
        self.queue.append(packet)
        self.mpp[packet]=1
        if destination not in self.timestamps:
            self.timestamps[destination]=[]
        self.timestamps[destination].append(timestamp)
        return True
    
    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        res=self.queue.popleft()
        del self.mpp[res]
        temp=res[1]
        self.st[temp]=self.st.get(temp,0)+1
        return list(res)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.timestamps:
            return 0
        a=self.timestamps[destination]
        temp=self.st.get(destination,0)
        right=bisect.bisect_left(a,startTime,temp)
        left=bisect.bisect_right(a,endTime,temp)
        return left-right
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)