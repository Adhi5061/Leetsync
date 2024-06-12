class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        queue = deque([(sr,sc)])
        visited = {(sr,sc)}
        image[sr][sc] = color
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                if i-1 >= 0 and image[i-1][j] == oldColor and (i-1, j) not in visited:
                    image[i-1][j] = color
                    queue.append((i-1,j))
                    visited.add((i-1,j))
                if j-1 >= 0 and image[i][j-1] == oldColor and (i, j-1) not in visited:
                    image[i][j-1] = color
                    queue.append((i,j-1))
                    visited.add((i,j-1))
                if i+1 < m and image[i+1][j] == oldColor and (i+1, j) not in visited:
                    image[i+1][j] = color
                    queue.append((i+1,j))
                    visited.add((i+1,j))
                if j+1 < n and image[i][j+1] == oldColor and (i, j+1) not in visited:
                    image[i][j+1] = color
                    queue.append((i,j+1))
                    visited.add((i,j+1))
                
        return image