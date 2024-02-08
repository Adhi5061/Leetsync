# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """if(root==None):
            return 0
        if(root.val>high):
            return(self.rangeSumBST(root.left,low,high))
        if(root.val<low):
            return(self.rangeSumBST(root.right,low,high))
        else:
            return(root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high))
        """
        curr=root
        stack=[]
        res=0
        while curr or stack:
            while(curr):
                if(curr.val>=low and curr.val<=high):
                    res+=curr.val
                stack.append(curr)
                curr=curr.left
            curr=stack.pop().right
        return res
            

        