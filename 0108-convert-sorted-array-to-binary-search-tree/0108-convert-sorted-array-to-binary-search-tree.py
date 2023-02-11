# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def makeTree(target: List[int]):
            if len(target) == 0:
                return None
            mid = int(len(target) / 2)
            node = TreeNode(target[mid])
            if mid > 0:
                node.left = makeTree(target[:mid])
                node.right = makeTree(target[mid+1:])
            return node

        return makeTree(nums)
        