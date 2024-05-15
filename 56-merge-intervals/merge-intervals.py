class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda d:(d[0]))
        i=0
        j=i+1
        while(j<len(intervals)):
            if(intervals[j][0]<=intervals[i][1]):
                intervals[i][1]=max(intervals[j][1],intervals[i][1])
                intervals.pop(j)
            else:
                i+=1
                j+=1
        return intervals