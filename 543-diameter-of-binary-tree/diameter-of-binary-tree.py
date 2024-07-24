# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans=0
        def dia(root):
            if(root==None):
                return 0
            left=dia(root.left)
            right=dia(root.right)
            self.ans=max(self.ans,left+right)
            return 1+max(left,right)
        dia(root)
        return self.ans    
        # self.dia=0
        # def diameter(root):
        #     if(root==None):
        #         return 0
        #     l=diameter(root.left)
        #     r=diameter(root.right)
        #     cdia=l+r
        #     self.dia=max(self.dia,cdia)
        #     height=max(l,r)+1
        #     return height
        # diameter(root)
        # return self.dia