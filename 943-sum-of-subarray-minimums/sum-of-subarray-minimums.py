class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pse=[]
        stack=[]
        for i in range(0,len(arr)):
            while(stack and arr[stack[-1]]>arr[i]):
                stack.pop()
            pse.append(stack[-1] if stack else -1)
            stack.append(i)
        nse=[]
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while(stack and arr[stack[-1]]>=arr[i]):
                stack.pop()
            nse.append(stack[-1] if stack else len(arr))
            stack.append(i)
        nse=nse[::-1]
        print(pse,"\n",nse)
        res=0
        for i in range(0,len(arr)):
            left=i-pse[i]
            right=nse[i]-i
            tc=left*right%(10**9+7)
            c=tc*arr[i]%(10**9+7)
            res=res+c%(10**9+7)
            # print(left,right,c)
        return res%(10**9+7)