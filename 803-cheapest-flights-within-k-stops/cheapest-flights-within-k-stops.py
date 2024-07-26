
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        from collections import deque
        q=deque()
        q.append((0,0,src))
        distance=[float("inf")]*n 
        distance[src]=0
        adj=[[] for _ in range(n)]
        for start,end,weight in flights:
            adj[start].append((end,weight))
        while(q):
            stop,dist,node=q.popleft()
            for nd,weight in adj[node]:
                if(stop<=K and dist+weight<distance[nd]):
                    distance[nd]=min(distance[nd],dist+weight)
                    q.append((stop+1,distance[nd],nd))
        # print(distance)
        if(distance[dst]==float("inf")):
            return -1
        return distance[dst]