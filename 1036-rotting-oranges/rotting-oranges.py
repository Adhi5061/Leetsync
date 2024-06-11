from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        
        def bfs():
            maxt=0
            q=Queue()
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    if(grid[i][j]==2):
                        q.put((i,j,0))
            while(not q.empty()):
                # print(q,end="next")
                node=q.get()
                for i in range(4):
                    # print(node)
                    nx=node[0]+x[i]
                    ny=node[1]+y[i]
                    if(nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]) and grid[nx][ny]==1):
                        grid[nx][ny]=2
                        q.put((nx,ny,node[2]+1))
                        maxt=max(maxt,node[2]+1)
            return maxt

        maxt=bfs()
        print(grid)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    return -1
        return maxt