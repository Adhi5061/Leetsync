# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #Recursive Solution 

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

        #While loop 

        # q=[(root,1)]
        # if(root==None):
        #     return 0
        # curr=None
        # maxv=0
        # while(q):
        #     curr,ind=q.pop(0)
        #     maxv=max(maxv,ind)
        #     if(curr.left):
        #         q.append([curr.left,ind+1])
        #     if(curr.right):
        #         q.append([curr.right,ind+1])
        # return maxv

        #For Loop

        if(root==None):
            return 0
        q=[root]
        level=0
        while(q):
            for i  in range(len(q)):
                curr=q.pop(0)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            level+=1
        return level