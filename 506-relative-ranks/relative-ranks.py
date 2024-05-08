import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=list(score)
        heapq.heapify(temp)
        ans=heapq.nlargest(3,temp)
        d={}
        for i in range(0,len(score)):
            d[score[i]]=i
        res=[0]*len(score)
        pos=len(score)
        print(d)
        while(len(temp)>0):
            a=heapq.heappop(temp)
            print(a)
            if(a==ans[0]):
                res[d[a]]=("Gold Medal")
            elif(a==ans[1]):
                res[d[a]]=("Silver Medal")
            elif(a==ans[2]):
                res[d[a]]=("Bronze Medal")
            else:
                res[d[a]]=(str(pos))
                pos-=1
        return res