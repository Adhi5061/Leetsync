class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        def palindrome(i,arr):
            if(i==len(s)):
                res.append(arr[:])
            for j in range(i,len(s)):
                if(s[i:j+1]==s[i:j+1][::-1]):
                    arr.append(s[i:j+1])
                    palindrome(j+1,arr)
                    arr.pop()
        palindrome(0,[])
        return res
        # def palindrome(curr,i,arr,flag):
        #     # print(curr,i,arr)
        #     if(i==len(s)):
        #         if(flag):
        #             res.append(arr[:])
        #         return
        #     curr+=s[i]
        #     if(curr==curr[::-1]):
        #         arr.append(curr)
        #         palindrome("",i+1,arr,1)
        #         arr.pop()
        #     palindrome(curr,i+1,arr,0)
        # palindrome("",0,[],0)
        # return res
