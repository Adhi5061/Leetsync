# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root==None):
            return True
        def balanced(root):
            if(root==None):
                return [True,0]
            l=balanced(root.left)
            r=balanced(root.right)
            if(not l[0] or not r[0]):
                return [False,l]
            if(abs(l[1]-r[1])<2):
                return [True,max(l[1],r[1])+1]
            else:
                return [False,l]
        return balanced(root)[0]