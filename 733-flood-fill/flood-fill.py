from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        start = image[sr][sc]
        
        # If the starting color is the same as the new color, return the original image
        if start == color:
            return image
        
        res = [row[:] for row in image]  # Make a deep copy of the original image

        def bfs():
            q = deque([(sr, sc)])
            while q:
                curr = q.popleft()
                res[curr[0]][curr[1]] = color
                image[curr[0]][curr[1]] = -1  # Mark the cell as visited by setting it to -1
                
                for i in range(4):
                    cx = curr[0] + x[i]
                    cy = curr[1] + y[i]
                    if 0 <= cx < len(image) and 0 <= cy < len(image[0]) and image[cx][cy] == start:
                        q.append((cx, cy))
                        image[cx][cy] = -1  # Mark the cell as visited

        bfs()
        return res
