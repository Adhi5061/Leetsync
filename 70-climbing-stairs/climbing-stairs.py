class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        # if(n<3):
        #     memo[n]=n
        #     return n
        # if(n in memo):
        #     return memo[n]
        # res=(self.climbStairs(n-1)+self.climbStairs(n-2))
        # memo[n]=res
        # return res
        table=[0]*(n+1)
        table[0]=1
        table[1]=1
        for i in range(2,len(table)):
            print(i)
            table[i]=table[i-1]+table[i-2]
        return table[n]