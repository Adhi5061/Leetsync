class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        d={}
        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1
        print(m,n)
        def path(x,y):
            if((x,y) in d):
                return d[(x,y)]
            if(x>m or y>n):
                return 0
            if(obstacleGrid[x][y]==1):
                d[(x,y)]=0
                return 0
            if(x==m and y==n):
                d[(x,y)]=1
                return 1
            else:
                ans= (path(x+1,y)+path(x,y+1))
                d[(x,y)]=ans
                return ans
        return path(0,0)