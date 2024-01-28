import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d=collections.deque()
        for index,value in enumerate(nums):   
            while(d and value>nums[d[-1]]):
                d.pop()
            d.append(index)
            if(index-d[0]>=k):
                d.popleft()
            if(index<k-1):
                continue
            res.append(nums[d[0]])
        return res