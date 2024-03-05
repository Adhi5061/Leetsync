class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        if(n<3):
            memo[n]=n
            return n
        if(n in memo):
            return memo[n]
        res=(self.climbStairs(n-1)+self.climbStairs(n-2))
        memo[n]=res
        return res