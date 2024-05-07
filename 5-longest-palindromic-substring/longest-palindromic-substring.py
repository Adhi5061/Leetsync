class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check(i,j):
            while(i>=0 and j<len(s)):
                if(s[i]==s[j]):
                    i-=1
                    j+=1
                else:
                    break
            return (i+1,j-1)
        maxv=0
        res=""
        for i in range(0,len(s)):
            a=check(i-1,i+1)
            # print(a)
            if(a[1]-a[0]+1>=maxv):
                maxv=a[1]-a[0]+1
                res=s[a[0]:a[1]+1]
            # print(i,len(s))
            if(i<(len(s)-1) and s[i]==s[i+1]):
                a=check(i-1,i+2)
                if(a[1]-a[0]+1>maxv):
                    maxv=a[1]-a[0]+1
                    res=s[a[0]:a[1]+1]
        return res
        # i=0
        # count=0
        # while(i<len(s)):
        #     j=i+1
        #     while(j<=len(s)):
        #         if(s[i:j]==s[i:j][::-1]):
        #             if(j-i>count):
        #                 res=s[i:j]
        #                 count=j-i
        #         j+=1
        #     i+=1
        # print(count)
        # return res
