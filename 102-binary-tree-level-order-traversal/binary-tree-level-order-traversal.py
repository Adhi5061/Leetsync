# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res=[]
        # def level(root,i):
        #     if(root==None):
        #         return
        #     if(i>=len(res)):
        #         res.append([root.val])
        #     else:
        #         res[i].append(root.val)
        #     level(root.left,i+1)
        #     level(root.right,i+1)
        # level(root,0)
        # return res
        res=[]
        if(root==None):
            return []
        q=[(root,0)]
        while(q ):
            curr,ind=q.pop(0)
            if(ind<len(res)):
                res[ind].append(curr.val)
            else:
                res.append([curr.val])
            if(curr.left):
                q.append((curr.left,ind+1))
            if(curr.right):
                q.append((curr.right,ind+1))
        return res