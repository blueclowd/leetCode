/**
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
 */
int* getRow(int rowIndex, int* returnSize) {

    int* const row = (int*)malloc(sizeof(int)*(rowIndex+1));

    *returnSize = rowIndex+1;

    int idx;
    for(idx = 0; idx<=rowIndex; idx++)
    {
        row[idx] = combination(rowIndex, idx);
    }

    return row;

}

int combination(int n, int k)
{
    double result = 1;
    while(n != (n-k))
    {
        result *= n;
        result /= k;

        n--;
        k--;
    }

    return round(result);
}
