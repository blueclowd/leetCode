#include <stdbool.h>

/**
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
*/

int cmp(const void* a, const void* b)
{
    return *(int*)a - *(int*)b;
}

bool containsDuplicate(int* nums, int numsSize)
{

    qsort(nums, numsSize, sizeof(int), cmp);

    int idx;
    for(idx = 0; idx<numsSize-1; ++idx)
    {
        if (nums[idx] == nums[idx+1])
        {
            return true;
        }
    }

    return false;
}
