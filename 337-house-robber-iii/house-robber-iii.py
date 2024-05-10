# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def dp(root):
            if(root in memo):
                return memo[root]
            if(root==None):
                return 0
            # print(root.val)
            if(root.left==None and root.right==None):
                return root.val
            elif(root.left!=None and root.right!=None):
                a=root.val+dp(root.left.left)+dp(root.left.right)+dp(root.right.left)+dp(root.right.right)
                b=dp(root.left)+dp(root.right)
            elif(root.left==None):
                a=root.val+dp(root.right.left)+dp(root.right.right)
                b=dp(root.right)
            else:
                a=root.val+dp(root.left.left)+dp(root.left.right)
                b=dp(root.left)
            ans=max(a,b)
            # print(root.val,a,b,ans)
            memo[root]=ans
            return max(a,b)
        return dp(root)