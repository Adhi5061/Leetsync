# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[-float("inf")]
        def maxv(root):
            if(root==None):
                return 0
            left=maxv(root.left)
            right=maxv(root.right)
            res[0]=max(res[0],root.val+left+right,root.val,root.val+max(left,right))
            return max(root.val,root.val+max(left,right))
        maxv(root)
        return res[0]
        # self.cmax=-10000
        # def dfs(root):
        #     if(root==None):
        #         return 0
        #     l=dfs(root.left)
        #     r=dfs(root.right)
        #     cval=max(l+r+root.val,l+root.val,r+root.val,root.val)
        #     self.cmax=max(self.cmax,cval)
        #     return max(l+root.val,r+root.val,root.val)
        # dfs(root)
        # return self.cmax

        