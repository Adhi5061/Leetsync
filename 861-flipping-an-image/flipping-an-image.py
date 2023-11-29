class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(image)):
            image[i].reverse()
            for j in range(0,len(image[i])):
                image[i][j]=image[i][j]^1
        return image
        
        