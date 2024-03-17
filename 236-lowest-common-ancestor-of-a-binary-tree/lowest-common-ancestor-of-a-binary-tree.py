# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans=None
        def dfs(root):
            temp=0
            if(root==None):
                return 0
            if(root==p):
                temp=1
            if(root==q):
                temp=1
            temp+=dfs(root.left)+dfs(root.right)
            if(not self.ans and temp==2):
                self.ans=root
            return temp
        dfs(root)
        return self.ans