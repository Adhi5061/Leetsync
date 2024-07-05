from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*(len(isConnected))
        def dfs(node):
            # print(node,visited)
            visited[node]=1
            for i in range(0,len(isConnected)):
                if(isConnected[node][i]==1 and visited[i]==0):
                    dfs(i)
        
        res=0
        for i in range(len(isConnected)):
            if(visited[i]==0):
                dfs(i)
                res+=1
                # print(i,res)
        return res