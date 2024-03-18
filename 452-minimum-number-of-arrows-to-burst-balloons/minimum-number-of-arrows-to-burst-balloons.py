class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        res=0
        i=0
        t=0
        minv=points[i][1]
        while(i<len(points)):
            if(points[i][0]<=minv and points[i][1]>=minv):
                i+=1
                t=1
                continue
            else:
                minv=points[i][1]
                t=0
                res+=1
                print(points[i],minv)
        return res+t