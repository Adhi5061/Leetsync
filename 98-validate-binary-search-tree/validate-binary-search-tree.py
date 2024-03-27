# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        def bst(root,minv,maxv):
            if(root==None):
                return True
            if(root.val>minv and root.val<maxv):
                if(root.left and root.right ):
                    return bst(root.left,minv,root.val) and bst(root.right,root.val,maxv)
                if(root.left):
                    return bst(root.left,minv,root.val)
                if(root.right):
                    return bst(root.right,root.val,maxv)
                return True
            return False
        return bst(root,float("-inf"),float("inf"))
            

        # if(root==None):
        #     return True
        # if(root.left==None and root.right==None):
        #     return True
        # if(root.left and root.right):
        #     if(root.val>root.left.val and root.val<root.right.val):
        #         return self.isValidBST(root.left) and self.isValidBST(root.right)
        #     return False
        # if(root.left and root.val>root.left.val):
        #     return self.isValidBST(root.left)
        # if(root.right and root.val<root.right.val):
        #     return self.isValidBST(root.right)
        # return False