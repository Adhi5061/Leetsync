# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if(len(nums)==0):
            return None
        element = max(nums)
        maxi = nums.index(element)
        node=TreeNode(nums[maxi])
        node.left=self.constructMaximumBinaryTree(nums[0:maxi])
        node.right=self.constructMaximumBinaryTree(nums[maxi+1:])
        return node
