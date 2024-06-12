from queue import Queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        start=image[sr][sc]
        res=[row[:] for row in image]
        visited=set()
        def bfs():
            q=Queue()
            q.put((sr,sc))
            while(not q.empty()):
                # print(q)
                curr=q.get()
                res[curr[0]][curr[1]]=color
                image[curr[0]][curr[1]]=-1
                for i in range(4):
                    cx=curr[0]+x[i]
                    cy=curr[1]+y[i]
                    if(cx>=0 and cy>=0 and cx<len(image)  and cy<len(image[0]) and image[cx][cy]!=-1  and image[cx][cy]==start):
                        q.put((cx,cy))
                        # visited.add((cx,cy))
        bfs()
        return res