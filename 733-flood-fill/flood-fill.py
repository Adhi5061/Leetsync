from queue import Queue
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        start = image[sr][sc]
        res = [row[:] for row in image]
        
        if start == color:
            return res
        
        q = Queue()
        q.put((sr, sc))
        visited = set()
        visited.add((sr, sc))
        
        while not q.empty():
            curr = q.get()
            res[curr[0]][curr[1]] = color
            
            for i in range(4):
                cx = curr[0] + x[i]
                cy = curr[1] + y[i]
                if (0 <= cx < len(image) and 0 <= cy < len(image[0]) and
                    (cx, cy) not in visited and image[cx][cy] == start):
                    q.put((cx, cy))
                    visited.add((cx, cy))
        return res
