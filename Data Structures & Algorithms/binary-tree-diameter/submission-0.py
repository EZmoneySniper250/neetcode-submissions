# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left_d = dfs(node.left)
            right_d = dfs(node.right)
            ans = max(ans, left_d+ right_d)
            return 1 + max(left_d, right_d)
        dfs(root)
        return ans
