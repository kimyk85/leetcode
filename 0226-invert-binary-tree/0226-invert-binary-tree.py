# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = collections.deque([root])

        while queue:
            for _ in range(len(queue)):
                cur_root = queue.popleft()

                cur_root.left, cur_root.right = cur_root.right, cur_root.left

                if cur_root.left is not None:
                    queue.append(cur_root.left)
                if cur_root.right is not None:
                    queue.append(cur_root.right)

        return root