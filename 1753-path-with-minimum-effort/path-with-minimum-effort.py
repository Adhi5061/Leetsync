class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        columns=len(heights[0])
        dist=[[float("inf")]*columns for _ in range(rows)]
        diff=float("inf")
        neigh=[(1,0),(0,1),(-1,0),(0,-1)]
        hq=[]
        dist[0][0]=0
        heapq.heappush(hq,(0,0))
        while hq:
            x,y=heapq.heappop(hq)
            # if(x==rows-1 and y=columns-1):
            #     dist=min(dist,d)
            #     continue
            for node in neigh:
                nx=x+node[0]
                ny=y+node[1]
                if(nx>=0 and ny>=0 and nx<rows and ny<columns):
                    t=max(abs(heights[nx][ny]-heights[x][y]),dist[x][y])
                    if(t<dist[nx][ny]):
                        dist[nx][ny]=t
                        heapq.heappush(hq,(nx,ny))
        return dist[rows-1][columns-1]