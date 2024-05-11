class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        
        memo={}
        def dp(ind):
            if(ind in memo):
                return memo[ind]
            d=dict()
            # print("sf",d)
            ans=10000
            if(ind==len(s)):
                return 0
            for i in range(ind,len(s)):
                d[s[i]]=d.get(s[i],0)+1
                val=list(d.values())[0]
                flag=True
                for indg,value in d.items():
                    if(val!=value):
                        flag=False
                        break
                if(flag):
                    ans=min(ans,1+dp(i+1))
            # print("answer",ans)
            memo[ind]=ans
            return ans
        return dp(0)