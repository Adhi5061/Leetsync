class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        memo={}
        def dp(ind):
            if(ind in memo):
                return memo[ind]
            if(ind==len(s)):
                return 0
            d={}
            ans=10**5
            for i in range(ind,len(s)):
                
                d[s[i]]=d.get(s[i],0)+1
                value=list(d.values())[0]
                flag=True
                # print(ind,i,d,ans)
                for indf,val in d.items():
                    if(val!=value):
                        flag=False
                        break
                if(flag):
                    p=dp(i+1)
                    ans=min(ans,1+p)
                # print("After",ind,ans)
            memo[ind]=ans
            return ans
        return dp(0)