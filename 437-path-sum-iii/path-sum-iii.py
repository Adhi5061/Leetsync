# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count=0
        def dfs(root,prefix):
            if(root==None):
                return
            if(root.val in prefix):
                self.count+=prefix.count(root.val)

            if(targetSum-root.val ==0):
                self.count+=1
            
            for i in range(len(prefix)):
                prefix[i]-=root.val
            
            prefix.append(targetSum-root.val)
            dfs(root.left,prefix)
            dfs(root.right,prefix)

            prefix.pop()
            for i in range(len(prefix)):
                prefix[i]+=root.val
        dfs(root,[])
        return self.count