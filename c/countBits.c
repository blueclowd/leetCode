/**
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
 */
int* countBits(int num, int* returnSize) {

    int *result = (int*)malloc(sizeof(int)*(num+1));
    memset(result, 0, sizeof(int)*(num+1));

    *returnSize = num+1;

    int i;
    for(i = 0; i <= num;i++)
    {
        result[i] = result[i/2] + i % 2;
    }

    return result;
}
