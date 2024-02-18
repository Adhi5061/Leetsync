class Solution:
    def beautySum(self, s: str) -> int:
        def csum(st):
            maxv=0
            minv=10000
            d={}
            for i in st:
                if(i in d):
                    d[i]+=1
                else:
                    d[i]=1
                if(d[i]>maxv):
                    maxv=d[i]
            for i in d:
                if(d[i]<minv):
                    minv=d[i]
            return maxv-minv
        count=0
        for i in range(0,len(s)-2):
            for j in range(i,len(s)):
                count+=csum(s[i:j+1])
        return count