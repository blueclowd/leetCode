#include <stdlib.h>
#include "functionInterface.h"
/**
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
*/
int maxDepth(struct TreeNode* root)
{

    if (root == NULL)
    {
        return 0;
    }

    const int leftDepth = maxDepth(root->left);
    const int rightDepth = maxDepth(root->right);

    return leftDepth > rightDepth ? leftDepth +1  : rightDepth +1 ;
}
