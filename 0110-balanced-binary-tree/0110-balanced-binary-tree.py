# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        def nodeDepth(node):
            if node:
                if node.left is None and node.right is None:
                    return 1

                node_left_depth = 0
                node_right_depth = 0
                if node.left:
                    node_left_depth = nodeDepth(node.left)
                if node.right:
                    node_right_depth = nodeDepth(node.right)

                if node_left_depth >= 0 and node_right_depth >= 0:
                    if abs(node_left_depth - node_right_depth) < 2:
                        return max(node_left_depth, node_right_depth) + 1
                    else:
                        return -1
                else:
                    return -1
            else:
                return 0

        if nodeDepth(root) > 0:
            return True
        else:
            return False
        