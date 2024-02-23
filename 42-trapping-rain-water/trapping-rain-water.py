class Solution:
    def trap(self, height) :
        lh=[]
        rh=[]
        cg=-1
        for ind,val in enumerate(height):
            if(val>=cg):
                lh.append(-1)
                cg=val
            else:
                lh.append(cg)
        cg=-1
        for i in range(len(height)-1,-1,-1):
            if(height[i]>=cg):
                rh.append(-1)
                cg=height[i]
            else:
                rh.append(cg)
        rh.reverse()
        store=0
        for i in range(0,len(height)):
            if(lh[i]!=-1 and rh[i]!=-1):
                store+=(min(lh[i],rh[i])-height[i])
        return store