class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        from collections import deque
        visited=[0]*len(isConnected)
        q=deque()
        res=0
        def bfs(node):
            q.append(node)
            visited[node]=1
            while(q):
                n=q.popleft()
                for i in range(0,len(isConnected)):
                    if(isConnected[n][i]==1 and visited[i]==0):
                        visited[i]=1
                        q.append(i)
        for i in range(0,len(isConnected)):
            if(not visited[i]):
                res+=1
                bfs(i)
        return res