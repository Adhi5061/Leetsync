class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        s1=set()
        s2=set()
        for i in range(0,len(matrix)):
            mine=matrix[i][0]
            for j in range(0,len(matrix[0])):
                mine=min(matrix[i][j],mine)
            s1.add(mine)
        for i in range(0,len(matrix[0])):
            maxe=matrix[0][i]
            for j in range(0,len(matrix)):
                maxe=max(maxe,matrix[j][i])
            s2.add(maxe)
        return list(s1&s2)