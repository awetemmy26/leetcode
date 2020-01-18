# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if max(q.val, p.val) < root.val:
            return self.lowestCommonAncestor(root.left, q, p)
        if min(q.val, p.val) > root.val:
            return self.lowestCommonAncestor(root.right, q, p)
        return root
# @lc code=end
