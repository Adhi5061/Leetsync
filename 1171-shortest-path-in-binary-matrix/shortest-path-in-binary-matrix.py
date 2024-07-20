from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ind=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        q=deque()
        source=(0,0)
        if(grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1):
            return -1
        destination=(len(grid)-1,len(grid[0])-1)
        if(source==destination):
            return 1
        q.append((source[0],source[1],1))
        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        visited[source[0]][source[1]]=1
        while(q):
            cx,cy,d=q.popleft()
            for i in range(8):
                nx=cx+ind[i][0]
                ny=cy+ind[i][1]
                if(nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]==0 and not visited[nx][ny]):
                    if(nx==destination[0] and ny==destination[1]):
                        return d+1
                    else:
                        visited[nx][ny]=1
                        q.append((nx,ny,d+1))
        return -1