from queue import Queue
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)

        # def dfs(node):
        #     if(visited[node]):
        #         return
        #     visited[node]=1
        #     for i in range(0,len(isConnected[node])):
        #         if(isConnected[node][i]==1):
        #             dfs(i)
        def bfs(node):
            q=Queue()
            visited[node]=1
            q.put(node)
            while(not q.empty()):
                n=q.get()
                visited[n]=1
                for i in range(0,len(isConnected)):
                    if(i!=n and isConnected[n][i]==1 and visited[i]==0):
                        q.put(i)

        res=0
        for i in range(0,len(visited)):
            if(visited[i]==0):
                bfs(i)
                res+=1
        return res