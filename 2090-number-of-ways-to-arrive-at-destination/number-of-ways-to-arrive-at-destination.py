class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        import heapq
        adj=[[] for _ in range(n)]
        for start,end,weights in roads:
            adj[start].append((end,weights))
            adj[end].append((start,weights))
        ways=[0]*n
        ways[0]=1
        distance=[float("inf")]*n
        distance[0]=0
        q=[(0,1,0)]
        while(q):
            dist,way,node=heapq.heappop(q)
            for nd,weight in adj[node]:
                if(dist+weight==distance[nd]):
                    ways[nd]+=ways[node]
                    # heapq.heappush(q,(distance[nd],ways[nd],nd))
                if(dist+weight<distance[nd]):
                    ways[nd]=ways[node]
                    distance[nd]=dist+weight
                    heapq.heappush(q,(distance[nd],ways[nd],nd))
        # print(distance)
        # print(ways)
        return ways[n-1]%(10**9+7)