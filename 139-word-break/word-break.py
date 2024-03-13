class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo={}
        def dfs(curr):
            if(curr==""):
                return True
            if(curr in memo):
                return memo[curr]
            temp=""
            flag=False
            for ind,i in enumerate(curr):
                temp+=i
                if(temp in wordDict):
                    flag=flag or dfs(curr[ind+1:])
                    if(flag):
                        memo[curr]=True
                        return True
            memo[curr]=False
            return False
        return dfs(s)