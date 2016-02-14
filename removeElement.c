
/**
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/
int removeElement(int* nums, int numsSize, int val)
{

    int nextIdx = 0;

    int idx;

    for(idx = 0; idx<numsSize; idx++)
    {
        if (nums[idx] != val)
        {
            nums[nextIdx] = nums[idx];

            if (idx != nextIdx)
            {
                nums[idx] = 0;
            }

            nextIdx++;
        }
    }

    return nextIdx;
}
