# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def searchnode(node):
            if node:
                if node.val >= low and node.val <= high:
                    # self.result.append(node.val)
                    self.result += node.val
                    searchnode(node.left)
                    searchnode(node.right)
                elif node.val < low:
                    searchnode(node.right)
                elif node.val > high:
                    searchnode(node.left)

        searchnode(root)
        return self.result
        