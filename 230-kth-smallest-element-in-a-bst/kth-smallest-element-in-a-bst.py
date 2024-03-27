# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=0
        def dfs(root,curr):
            if(root==None):
                return curr
            # print(root.val,curr)
            curr=dfs(root.left,curr)
            curr+=1
            print(root.val,curr)
            if(k==curr):
                print(root.val)
                self.ans= root.val
            curr=dfs(root.right,curr)
            return curr
        dfs(root,0)
        return self.ans