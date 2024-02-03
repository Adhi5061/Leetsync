class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if(len(s)<2):
            return ""
        ss=set(s)
        t=1
        for ind,char in enumerate(s):
            if(char.swapcase() in s):
                continue
            else:
                t=0
                break
        if(t==1):
            return s
        else:
            return(max(self.longestNiceSubstring(s[0:ind]),self.longestNiceSubstring(s[ind+1:]),key=len))
