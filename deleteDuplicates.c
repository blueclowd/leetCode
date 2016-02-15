#include <stdlib.h>
#include "functionInterface.h"

/**
Given a sorted linked list, delete all duplicates such that each element appear only once.
*/
typedef struct ListNode* NodePtr;

struct ListNode* deleteDuplicates(struct ListNode* head) {

    // Pointer to the current node
    NodePtr p = head;

    // Pointer to the duplicated node
    NodePtr toBeDel;

    // Pointer to the next of current node
    NodePtr nextNode;

    while (p != NULL)
    {
        nextNode = p->next;

        if (nextNode != NULL && p->val == nextNode->val)
        {
            toBeDel = nextNode;

            p->next = nextNode->next;

            free(toBeDel);
        }
        else
        {
            p = p->next;
        }
    }

    return head;

}
