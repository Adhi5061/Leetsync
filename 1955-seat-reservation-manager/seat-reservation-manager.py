import heapq
class SeatManager:

    def __init__(self, n: int):
        self.heap=[]
        self.curr=0

    def reserve(self) -> int:
        if(self.heap):
            return heapq.heappop(self.heap)
        self.curr+=1
        return self.curr

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)