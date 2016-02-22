#include <stdlib.h>
#include "functionInterface.h"
/**
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
 */

typedef struct ListNode* NodePtr;
struct ListNode* oddEvenList(struct ListNode* head) {

    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    NodePtr leadCurrentOdd = head->next;

    // Initial: the 3rd node
    NodePtr currentOdd = head->next->next;

    NodePtr currentInsert = head;

    NodePtr currentNext;

    while(currentOdd != NULL && leadCurrentOdd != NULL)
    {

        // Back up
        currentNext = currentInsert->next;


        currentInsert->next = currentOdd;
        leadCurrentOdd->next = currentOdd->next;
        currentOdd->next = currentNext;

        // Update pointers
        currentInsert = currentInsert->next;


        leadCurrentOdd = leadCurrentOdd->next;
        if (leadCurrentOdd == NULL)
        {
            break;
        }
        currentOdd = leadCurrentOdd->next;

    }

    return head;
}

