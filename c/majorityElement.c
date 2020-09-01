
/**
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
*/

int cmp(const void*, const void*);

int majorityElement(int* nums, int numsSize) {

    qsort(nums, numsSize, sizeof(int), cmp);

    int maxNum = 1;

    int major = nums[0];

    int currentNum = 1;

    int idx;
    for (idx = 1; idx<numsSize; idx++)
    {
        if (nums[idx-1] != nums[idx])
        {
            if (currentNum > maxNum)
            {
                major = nums[idx-1];
                maxNum = currentNum;
            }

            currentNum = 1;
        }
        else
        {
            currentNum++;
        }
    }

    // The last section
    if (currentNum > maxNum)
    {
        major = nums[numsSize-1];
    }

    printf("Major = %d \n", major);

    return major;

}

int cmp(const void* a, const void* b)
{
    return *(int*)a - *(int*)b;
}

