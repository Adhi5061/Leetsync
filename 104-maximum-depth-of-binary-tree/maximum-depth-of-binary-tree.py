# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if(root==None):
        #     return 0
        # l=self.maxDepth(root.left)
        # r=self.maxDepth(root.right)
        # return(max(l,r)+1)
        # if(root==None):
        #     return 0
        # l=self.maxDepth(root.left)
        # r=self.maxDepth(root.right)
        # return max(l,r)+1
        q=[(root,1)]
        if(root==None):
            return 0
        curr=None
        maxv=0
        while(q):
            curr,ind=q.pop(0)
            maxv=max(maxv,ind)
            if(curr.left):
                q.append([curr.left,ind+1])
            if(curr.right):
                q.append([curr.right,ind+1])
        return maxv