class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        q=deque()
        indeg=[0]*numCourses
        adj=[[] for row in range(numCourses)]
        for after,prev in prerequisites:
            adj[prev].append(after)
        # print(adj)
        for row in prerequisites:
            indeg[row[0]]+=1
        for ind in range(numCourses):
            if(indeg[ind]==0):
                q.append(ind)
        res=[]
        while(q):
            course=q.popleft()
            res.append(course)
            for node in adj[course]:
                indeg[node]-=1
                if(indeg[node]==0):
                    q.append(node)
        return res if len(res)==numCourses else []