/*
 * @lc app=leetcode.cn id=102 lang=cpp
 *
 * [102] 二叉树的层序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result {};
        search_tree(root, &result, 0);
        return result;
    }

    void search_tree(TreeNode* root, vector<vector<int>>* result, int level) {
        if (root == nullptr)
            return
        
        if (result->size() >= level) {
            result->push_back(vector<int>({}));
        }
            

        *result[level].push_back(root.val);

        if (root->left) {
            search_tree(root->left, result, level + 1);
        }
            
        if (root->right) {
            search_tree(root->right, result, level + 1);
        }
            
    }
};
// @lc code=end

