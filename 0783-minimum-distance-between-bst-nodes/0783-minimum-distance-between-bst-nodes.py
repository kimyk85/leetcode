# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    minValue = math.inf
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def searchvalue(node):
            import math
            leftmin, leftMax, rightmin, rightMax = math.inf,-math.inf,math.inf,-math.inf
            leftValue, rightValue = math.inf, math.inf
            if node.left:
                leftmin, leftMax = searchvalue(node.left)
            if node.right:
                rightmin, rightMax = searchvalue(node.right)

            if leftMax > -math.inf:
                leftValue = node.val - leftMax
            if rightmin < math.inf:
                rightValue = rightmin - node.val

            self.minValue = min(self.minValue, leftValue, rightValue)

            return min(leftmin, node.val), max(node.val, rightMax)

        searchvalue(root)
        return self.minValue
        