class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        memo={}
        def dp(i):
            if(i in memo):
                return memo[i]
            if(i>=len(arr)):
                return 0
            temp=0
            for j in range(1,k+1):
                if(i+j>len(arr)):
                    break
                temp=max(temp,max(arr[i:i+j])*j+dp(i+j))
                # print(i,j,temp)
            memo[i]=temp
            return temp
        return dp(0)