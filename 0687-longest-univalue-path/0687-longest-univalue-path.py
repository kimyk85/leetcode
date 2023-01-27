# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_c = -1
            r_c = -1
            l_l = 0
            r_l = 0
            if node.left:
                l_c, l_l = dfs(node.left)
                if node.val != node.left.val:
                    l_c = -1
            if node.right:
                r_c, r_l = dfs(node.right)
                if node.val != node.right.val:
                    r_c = -1

            length = l_c + r_c + 2
            c = max(l_c, r_c) + 1
            max_length = max(length, l_l, r_l)

            return c, max_length

        c, max_length = dfs(root)
        return max_length