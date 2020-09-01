#include <stdlib.h>
#include "functionInterface.h"
/**
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 */
int minDepth(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }

    int leftDepth = minDepth(root->left);
    int rightDepth = minDepth(root->right);

    if (leftDepth == 0)
    {
        return rightDepth+1;
    }

    if (rightDepth == 0)
    {
        return leftDepth+1;
    }

    return leftDepth > rightDepth ? rightDepth+1 : leftDepth+1;

}
