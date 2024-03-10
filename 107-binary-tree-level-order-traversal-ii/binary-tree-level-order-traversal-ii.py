# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #Reversing the normal bfs traversal
        # res=[]
        # def levelo(root,level):
        #     if(root==None):
        #         return 
        #     if(level<len(res)):
        #         res[level].append(root.val)
        #     else:
        #         res.append([root.val])
        #     levelo(root.left,level+1)
        #     levelo(root.right,level+1)
        # levelo(root,0)
        # return res[::-1]

        if(root==None):
            return []
        res=[]
        q=[root]
        while(q):
            temp=[]
            for i in range(len(q)):
                curr=q.pop(0)
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            res.insert(0,temp)
        return res