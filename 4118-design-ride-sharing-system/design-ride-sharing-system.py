class RideSharingSystem:

    def __init__(self):
        self.rider=deque()
        self.driver=deque()
    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)
    def matchDriverWithRider(self) -> List[int]:
        if self.rider and self.driver:
            y,x=self.rider.popleft(),self.driver.popleft()
            return [x,y]
        return [-1,-1]
    def cancelRider(self, riderId: int) -> None:
        if riderId not in self.rider:
            return 
        self.rider.remove(riderId)



# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)