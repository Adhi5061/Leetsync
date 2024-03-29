# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lis=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """if(root==None):
            return self.lis
        self.inorderTraversal(root.left)
        self.lis.append(root.val)
        return(self.inorderTraversal(root.right))"""
        res=[]
        curr=root
        stack=[]
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr=curr.left   
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res