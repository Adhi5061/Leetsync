class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            n=int(i)
            while(stack and stack[-1]>n and k>0):
                stack.pop()
                k-=1
                if(k==0):
                    break
            stack.append(n)
        while(k>0):
            stack.pop()
            k-=1
        # print(stack)
        res=""
        i=0
        flag=False
        for char in stack:
            if(str(char)=="0" and not flag):
                continue
            res+=str(char)
            flag=True
        return res if(len(res)>0) else "0"