class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        xc=[0,0,1,-1]
        yc=[1,-1,0,0]
        
        def bfs(q):
            l=0
            while(q):
                curr=q.popleft()
                x=curr[0]
                y=curr[1]
                l=curr[2]
                for i in range(4):
                    cx=x+xc[i]
                    cy=y+yc[i]
                    if(cx>=0 and cy>=0 and cx<len(grid) and cy<len(grid[0]) and grid[cx][cy]==1):
                        grid[cx][cy]=2
                        q.append((cx,cy,l+1))
            return l
        q=deque()
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==2):
                    q.append((i,j,0))
        # print(q)
        res=bfs(q)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    return -1
        return res