# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(root,curr):
            if(root==None):
                return
            if(root.left==None and root.right==None):
                res.append(curr+chr(97+root.val))
                return 
            dfs(root.left,curr+chr(97+root.val))
            dfs(root.right,curr+chr(97+root.val))
        dfs(root,"")
        for i in range(0,len(res)):
            res[i]=res[i][::-1]
        res.sort()
        return res[0]