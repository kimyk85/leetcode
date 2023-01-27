# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            l_c = -1
            r_c = -1
            l_l = 0
            r_l = 0
            if node.left:
                l_c, l_l = dfs(node.left)
            if node.right:
                r_c, r_l = dfs(node.right)

            length = l_c + r_c + 2
            c = max(l_c, r_c) + 1
            max_length = max(length, l_l, r_l )
            # self.max_length = max(self.max_length, length)

            return c, max_length

        c, max_length = dfs(root)
        return max_length
        