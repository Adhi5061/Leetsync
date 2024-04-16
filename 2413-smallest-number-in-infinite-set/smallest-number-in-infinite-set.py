import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[1]
        self.last=2

    def popSmallest(self) -> int:
        a=heapq.heappop(self.heap)
        if(self.last not in self.heap):
            heapq.heappush(self.heap,self.last)
        self.last+=1
        return a

    def addBack(self, num: int) -> None:
        if(num not in self.heap):
            heapq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)