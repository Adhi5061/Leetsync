class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while(left<=right):
            mid=(left+right)//2
            dayc=0
            cweight=0
            for weight in weights:
                if(cweight+weight>mid):
                    dayc+=1
                    cweight=weight
                else:
                    cweight+=weight
            dayc+=1
            print(mid,dayc)
            if(dayc>days):
                left=mid+1
            else:
                right=mid-1
        return left