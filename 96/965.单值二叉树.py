#
# @lc app=leetcode.cn id=965 lang=python
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def find_all_value(self, root, value):
        if root.val != value:
            return False
        
        if root.left:
            if not self.find_all_value(root.left, value):
                return False
        if root.right:
            
            if not self.find_all_value(root.right, value):
                return False

        return True
            

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return False

        return self.find_all_value(root, root.val)
        
# @lc code=end

