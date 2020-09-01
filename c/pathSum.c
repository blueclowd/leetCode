#include <stdbool.h>
#include <stdlib.h>
#include "functionInterface.h"

/**
 Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
 */
bool hasPathSum(struct TreeNode* root, int sum)
{
    if (root == NULL)
    {
        return false;
    }
    // Reach the the leaf node
    if(root->left == NULL && root->right == NULL)
    {
        // It is a valid path if the value of the leaf node equals to the remaining sum
        return root->val == sum;
    }
    else
    {
        // Subtract the current value from the remaining sum and pass down.
        // Return the union of the results from left and right
        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
    }
}
