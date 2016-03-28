/**
Given an array of integers, every element appears twice except for one. Find that single one.
*/
int singleNumber(int* nums, int numsSize) {

    int result = *nums;
    int i;
    for(i=1;i<numsSize;i++)
    {
        result ^= nums[i];
    }

    return result;
}
