class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minv=k
        left=right=0
        ki=0
        while(right<len(blocks)):
            if(blocks[right]=="W"):
                ki+=1
            if(right-left==k-1):
                minv=min(minv,ki)
                if(blocks[left]=="W"):
                    ki-=1
                left+=1
            right+=1
        return minv
                