class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res=0
        left=0
        right=0
        currcos=0
        while(right<len(s)):
            currcos+=abs(ord(s[right])-ord(t[right]))
            if(currcos>maxCost):
                currcos-=abs(ord(s[left])-ord(t[left]))
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res