# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(cur_root, cur_depth):
            if cur_root.left:
                left_depth = search(cur_root.left, cur_depth + 1)
            else:
                left_depth = cur_depth
            if cur_root.right:
                right_depth = search(cur_root.right, cur_depth + 1)
            else:
                right_depth = cur_depth

            return max(left_depth, right_depth)

        if root:
            return search(root, 1)
        else:
            return 0
