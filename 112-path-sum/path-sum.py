# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root==None):
            return False
        def dfs(root,csum,level):
            if(root==None):
                return False
            if(root.left==None and root.right==None):
                if(csum-root.val==0):
                    return True
                return False
            return(dfs(root.left,csum-root.val,level+1) or dfs(root.right,csum-root.val,level+1))
        return(dfs(root,targetSum,0))