import numpy as np
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(0,len(grid)):
            grid[i].sort(reverse=True)
        temp = np.transpose(grid)
        res=0
        for i in temp:
            res+=max(i)
        return res
        