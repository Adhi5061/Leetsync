class Solution:
    def trap(self, height: List[int]) -> int:
        lh=[]
        rh=[]
        stack=[]
        maxv=0
        for i in height:
            if(i>maxv):
                lh.append(0)
                maxv=i
            else:
                lh.append(maxv)
        maxv=0
        for i in range(len(height)-1,-1,-1):
            if(height[i]>maxv):
                rh.append(0)
                maxv=height[i]
            else:
                rh.append(maxv)
        res=0
        rh=rh[::-1]
        # print(lh,"\n",rh)
        for i in range(0,len(height)):
            t=min(lh[i],rh[i])
            res+=t-height[i] if(t!=0) else 0
        return res