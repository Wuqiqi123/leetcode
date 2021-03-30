#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search_tree(self, root, result, level):
        if not root:
            return 
        try:
            result[level].append(root.val)
        except:
            result.append([])
            result[level].append(root.val)
        
        if root.left:
            self.search_tree(root.left, result, level+1)
        if root.right:
            self.search_tree(root.right, result, level + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.search_tree(root, result, 0)
        return result

# @lc code=end

