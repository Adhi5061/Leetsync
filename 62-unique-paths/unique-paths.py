class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        def path(x,y):
            if((x,y) in d):
                return d[(x,y)]
            if(x==m or y==n):
                d[(x,y)]=1
                return 1
            else:
                ans= (path(x+1,y)+path(x,y+1))
                d[(x,y)]=ans
                return ans
        return(path(1,1))