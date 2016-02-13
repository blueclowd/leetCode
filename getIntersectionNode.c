
#include <stdlib.h>

#define NEXT(X) (X) = (X)->next

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{

    int lengthA = 0;
    int lengthB = 0;

    struct ListNode *ptrA = headA;
    struct ListNode *ptrB = headB;

    for (; ptrA != NULL; NEXT(ptrA))
    {
        lengthA++;
    }

    for (; ptrB != NULL; NEXT(ptrB))
    {
        lengthB++;
    }

    if (lengthA > lengthB)
    {
        int aIdx;
        for (aIdx = 0; aIdx<lengthA-lengthB; ++aIdx)
        {
            NEXT(headA);
        }

    }
    else
    {
        int bIdx;
        for(bIdx = 0; bIdx<lengthB-lengthA; ++bIdx)
        {
            NEXT(headB);
        }
    }

    while(headA != headB)
    {
        NEXT(headA);
        NEXT(headB);
    }

    return headA;

}
