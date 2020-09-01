#include <stdbool.h>
#include <limits.h>
#include "functionInterface.h"

/**
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
*/

void minStackCreate(MinStack *stack, int maxSize) {

    stack->topIdx = -1;
    stack->maxSize = maxSize;
    stack->values = (int*)malloc(sizeof(int)*maxSize);
    stack->min = INT_MAX;

}

void minStackPush(MinStack *stack, int element) {

    if (stack->topIdx < stack->maxSize)
    {
        stack->values[++stack->topIdx] = element;
    }

    if (element < stack->min)
    {
        stack->min = element;
    }
}

void minStackPop(MinStack *stack) {

    if (stack->topIdx >= 0)
    {
        int element = stack->values[stack -> topIdx];

        stack->topIdx--;

        int idx;
        int remainMin = INT_MAX;
        for (idx = 0; idx <= stack->topIdx; idx++)
        {
            if (stack->values[idx] < remainMin)
            {
                remainMin = stack->values[idx];
            }
        }

        stack->min = remainMin;
    }
}

int minStackTop(MinStack *stack) {

    if (stack->topIdx >=0)
    {
        return stack->values[stack->topIdx];
    }
}

int minStackGetMin(MinStack *stack) {

    return stack->min;
}

void minStackDestroy(MinStack *stack) {

    free(stack->values);
}
