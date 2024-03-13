class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo={}
        res=[]
        def dfs(curr,temp):
            print(temp,res)
            if(curr==""):
                res.append(temp)
            if(len(temp)!=0):
                temp+=" "
            t=""
            for i in range(0,len(curr)):
                t+=curr[i]
                summa=temp
                if(t in wordDict):
                    temp+=t
                    dfs(curr[i+1:],temp)
                temp=summa
        dfs(s,"")
        return res



        # def dfs(curr,string):
        #     if(curr==""):
        #         res.append(string)
        #         return True
        #     if(curr in memo):
        #         if(mem)
        #         res.append(string+" "+memo[curr])
        #         return memo[curr]
        #     temp=""
        #     flag=
        #     middstr=[]
        #     for ind,i in enumerate(curr):
        #         temp+=i
        #         if(temp in wordDict):
        #             flag=flag or dfs(curr[ind+1:],string)
        #             if(flag):
        #                 middstr.ex
        #                 memo[curr]=flag
        #                 return True
        #     memo[curr]=False
        #     return False
        # return dfs(s)