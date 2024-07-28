class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pse=[]
        stack=[]
        for i in range(0,len(heights)):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            pse.append(stack[-1] if stack else -1)
            stack.append(i)

        nse=[]
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            nse.append(stack[-1] if stack else len(heights))
            stack.append(i)
        nse=nse[::-1]
        maxv=0
        for i in range(0,len(heights)):
            t=nse[i]-pse[i]-1
            maxv=max(maxv,t*heights[i])

        return maxv
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        prefix=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(0,len(matrix[0])):
            prefix[0][i]=int(matrix[0][i])
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]=="0"):
                    prefix[i][j]=0
                else:
                    prefix[i][j]=prefix[i-1][j]+1
        maxv=0
        # print(prefix)
        for i in range(0,len(matrix)):
            maxv=max(maxv,self.largestRectangleArea(prefix[i]))
        return maxv