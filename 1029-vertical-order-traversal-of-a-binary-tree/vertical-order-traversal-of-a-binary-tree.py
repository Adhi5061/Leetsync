# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}

        def dfs(root,level,depth):
            if(root==None):
                return
            temp=[]
            if(level in d):
                dic=d[level]
                if(depth in dic):
                    dic[depth].append(root.val)
                else:
                    dic[depth]=[root.val]
            else:
                d[level]={depth:[root.val]}
            dfs(root.left,level-1,depth+1)
            dfs(root.right,level+1,depth+1)
        dfs(root,0,0)
        d=dict(sorted(d.items(),key=lambda x:(x[0],x[1])))
        print(d)
        res=[]
        for dicti in d.values():
            temp=[]
            dicti=dict(sorted(dicti.items()))
            for i in dicti:
                temp.extend(sorted(dicti[i]))
            res.append(temp)
        return res