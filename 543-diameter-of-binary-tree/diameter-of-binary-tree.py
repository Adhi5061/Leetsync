# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(root):
            if(root==None):
                return[0,0]
            l=diameter(root.left)
            r=diameter(root.right)
            cdia=abs(l[0]+r[0])
            print(l,r,cdia)
            dia=max(l[1],r[1],cdia)
            height=max(l[0],r[0])+1
            return [height,dia]
        return diameter(root)[1]