class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        d=dict(sorted(d.items(),key=lambda item:(-item[1],item[0])))
        # print(d)
        res=[]
        for i in d:
            res.append(i)
            k-=1
            if(k==0):
                break
        return res