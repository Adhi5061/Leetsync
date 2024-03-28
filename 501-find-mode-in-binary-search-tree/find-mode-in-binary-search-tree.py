# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}

        def dfs(root):
            if(root==None):
                return
            if(root.val in d):
                d[root.val]+=1
            else:
                d[root.val]=1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        print(d)
        res=[]
        maxv=d[list(d)[0]]
        for i in d:
            if(d[i]==maxv):
                res.append(i)
        return res