from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        q=deque()
        vis=[[0]*len(mat[0]) for row in mat]
        res=[row[:] for row in mat]
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                if(mat[i][j]==0):
                    q.append((i,j,0))
                    vis[i][j]=1
        while(q):
            curr=q.popleft()
            row=curr[0]
            col=curr[1]
            dist=curr[2]
            res[row][col]=dist
            for i in range(4):
                cx=row+x[i]
                cy=col+y[i]
                if(cx<0 or cy<0 or cx>=len(mat) or cy>=len(mat[0]) or vis[cx][cy]==1):
                    continue
                vis[cx][cy]=1
                q.append((cx,cy,dist+1))
        return res
        # for i in range(0,len(mat)):
        # res=[row[:] for row in mat]
        # x=[0,0,1,-1]
        # y=[1,-1,0,0]
        # def bfs(i,j):
        #     q=deque()
        #     q.append((i,j,0))
        #     while(q):
        #         curr=q.popleft()
        #         if(curr[0]<0 or curr[0]>=len(mat) or curr[1]<0 or curr[1]>=len(mat[0])):
        #             continue
        #         if(mat[curr[0]][curr[1]]==0):
        #             return curr[2]
        #         for i in range(4):
        #             q.append((curr[0]+x[i],curr[1]+y[i],curr[2]+1))
        # for i in range(0,len(mat)):
        #     for j in range(0,len(mat[0])):
        #         if(mat[i][j]!=0):
        #             res[i][j]=bfs(i,j)
        # return res