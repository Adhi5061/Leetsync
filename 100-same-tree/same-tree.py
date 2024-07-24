# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(root1,root2):
            if(root1==None and root2==None):
                return True
            if((root1 is None and root2 is not None) or (root1 is not None and root2 is None)):
                return False
            if(root1.val==root2.val):
                return(check(root1.left,root2.left) and check(root1.right,root2.right))
            return False
        return(check(p,q))