# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        


        def avg(root,lis,level,count):
            if(root==None):
                return
            if(len(lis)<=level):
                lis.append(root.val)
                count.append(1)
            else:
                lis[level]+=root.val
                count[level]+=1
            avg(root.left,lis,level+1,count)
            avg(root.right,lis,level+1,count)

        lis=[]
        coun=[]
        avg(root,lis,0,coun)
        res=[]
        for i,j in zip(lis,coun):
            res.append(i/j)
        return(res)

        