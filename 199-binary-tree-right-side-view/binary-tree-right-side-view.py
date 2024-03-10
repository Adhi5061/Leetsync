# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        def dfs(root,level,maxl):
            if(root==None):
                return maxl
            if(level>maxl):
                res.append(root.val)
                maxl=level
            maxl=dfs(root.right,level+1,maxl)
            maxl=dfs(root.left,level+1,maxl)
            return maxl
        dfs(root,0,-1)
        return res