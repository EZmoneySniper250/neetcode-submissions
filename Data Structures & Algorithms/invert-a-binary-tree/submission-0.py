# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # cur = [root]
        # ans = []
        # while cur:
        #     nxt = []
        #     vals = []
        #     for node in cur:
        #         vals.append(node.val)
        #         if node.left: 
        #             nxt.append(node.left)
        #         if node.right:
        #             nxt.append(node.right)
        #     ans += vals[::-1]
        #     cur = nxt
        # return ans
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        
        
        