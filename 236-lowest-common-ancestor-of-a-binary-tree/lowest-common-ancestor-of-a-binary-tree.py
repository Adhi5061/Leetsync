# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root==None):
            return None
        def dfs(rot):
            if(rot==None or rot==p or rot==q):
                return rot
            # print(rot.val)
            left=dfs(rot.left)
            right=dfs(rot.right)
            if(left and right):
                return rot
            else:
                # print(root.val)
                return left if left else right
        return dfs(root)