#include<stdlib.h>
/**
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
*/
int cmp(const void* a, const void* b)
{
    return *(int*)a - *(int*)b;
}

int missingNumber(int* nums, int numsSize)
{
    qsort(nums, numsSize, sizeof(int), cmp);
    int base = -1;

    int i;
    for(i = 0;i<numsSize;i++)
    {
        if (nums[i] - base != 1)
        {
            return base+1;
        }
        else
        {
            base = nums[i];
        }
    }
}


