class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo={}
        def dp(pos1,pos2):
            if((pos1,pos2) in memo):
                return memo[(pos1,pos2)]
            if(pos1==len(text1) or pos2==len(text2)):
                return 0
            a=0
            if(text1[pos1]==text2[pos2]):
                a=1+dp(pos1+1,pos2+1)
            b=dp(pos1+1,pos2)
            c=dp(pos1,pos2+1)
            memo[(pos1,pos2)]=max(a,b,c)
            return max(a,b,c)
        return dp(0,0)