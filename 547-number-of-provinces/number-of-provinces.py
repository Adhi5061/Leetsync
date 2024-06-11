
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        d={}
        for i in range(0,len(isConnected)):
            d[i]=[]
            for j in range(0,len(isConnected)):
                if(i!=j and isConnected[i][j]==1):
                    d[i].append(j)
        def dfs(node):
            if(visited[node]):
                return
            visited[node]=1
            for n in d[node]:
                dfs(n)
        # def dfs(node):
        #     if(visited[node]):
        #         return
        #     visited[node]=1
        #     for i in range(0,len(isConnected[node])):
        #         if(isConnected[node][i]==1):
        #             dfs(i)
        # def bfs(node):
        #     q=deque()
        #     visited[node]=1
        #     q.append(node)
        #     while(q):
        #         n=q.popleft()
        #         visited[n]=1
        #         for i in range(0,len(isConnected)):
        #             if(i!=n and isConnected[n][i]==1 and visited[i]==0):
        #                 q.append(i)

        res=0
        for i in range(0,len(visited)):
            if(visited[i]==0):
                dfs(i)
                res+=1
        return res