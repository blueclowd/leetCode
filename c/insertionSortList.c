#include <stdlib.h>
#include "functionInterface.h"

/**
Sort a linked list using insertion sort.
*/
struct ListNode* insertionSortList(struct ListNode* head) {

    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    struct ListNode *sorted, *preSorted, *unsorted, *next;

    // First node of unsorted list
    unsorted = head->next;

    // Separate sorted and unsorted list
    head->next = NULL;

    while (unsorted) {

        // Start from head
        sorted = head;
        preSorted = head;

        next = unsorted->next;

        int cnt = 0;
        while (sorted && sorted->val <= unsorted->val)
        {
            preSorted = sorted;
            sorted = sorted->next;

            cnt++;
        }

        if (sorted)
        {
            // Inserted in the front of the sorted list
            if (cnt == 0)
            {
                head = unsorted;
            }
            else
            {
                preSorted->next = unsorted;
            }

            unsorted->next = sorted;

        }
        else
        {
            // Inserted in the end of the sorted list
            unsorted->next = NULL;
            preSorted->next = unsorted;
        }
        unsorted = next;
    }
    return head;
}
