class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # if(sum(candies)<k):
        #     return 0
        # s=sum(candies)
        # if(k*min(candies)<=sum(candies)):
        #     return min(candies)
        left=0
        right=max(candies)
        mid=1
        pod=0
        while(left<=right):
            mid=(left+right)//2+(left+right)%2
            c=0
            if(mid==0):
                return 0
            for i in range(0,len(candies)):
                c+=candies[i]//mid
            # print(c,left,right,mid)
            # if(c==k):
            #     return mid
            if(c>=k):
                pos=mid
                left=mid+1
            else:
                right=mid-1
        return pos if pos else 0      