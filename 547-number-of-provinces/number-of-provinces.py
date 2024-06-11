class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)

        def dfs(node):
            if(visited[node]):
                return
            visited[node]=1
            for i in range(0,len(isConnected[node])):
                if(isConnected[node][i]==1):
                    dfs(i)

        res=0
        for i in range(0,len(visited)):
            if(visited[i]==0):
                dfs(i)
                res+=1
        return res