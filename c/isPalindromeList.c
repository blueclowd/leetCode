#include <stdlib.h>
#include <stdbool.h>
#include "functionInterface.h"
/**
Given a singly linked list, determine if it is a palindrome.
 */
typedef struct ListNode *NodePtr;

void reverseNode(NodePtr);

bool isPalindromeList(NodePtr head)
{

    if(head == NULL || head->next == NULL)
    {
        return true;
    }

    NodePtr orig = head, middle = head, last = head;

    // Get the last node
    int idx =0;
    while(last->next != NULL)
    {
        idx++;
        last = last->next;
    }

    idx = (idx+1)/2;

    // Get the middle node
    int i;
    for(i = 0;i<idx;++i)
    {
        middle = middle->next;
    }

    // Reverse the second part of list which starts from middle node
    reverseNode(middle);

    while(last != NULL)
    {
        printf("F = %d, B = %d \n", orig->val, last->val);

        // Check palindrome
        if(orig->val != last->val)
        {
            return false;
        }

        last = last->next;
        orig = orig->next;
    }

    return true;

}

void reverseNode(NodePtr head)
{
    if (head == NULL || head->next == NULL)
    {
        return;
    }

    NodePtr before = NULL;
    NodePtr current = head;
    NodePtr after = head->next;

    while(after != NULL)
    {
        NodePtr tmp = after->next;

        current->next = before;
        after->next = current;

        before = current;
        current = after;
        after = tmp;
    }

}
