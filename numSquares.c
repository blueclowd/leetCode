#include<limits.h>
#include<math.h>

/**
* Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
* For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
*/
int numSquares(int n)
{
    int* result = (int*)malloc(sizeof(int)*(n+1));

    int k;
    for (k = 0;k < n+1; k++)
    {
        result[k] = INT_MAX;
    }

    result[0] = 0;

    int i;
    for(i = 1; i <= n; ++i)
    {
        int j;

        for(j = 1; j <= sqrt(i); j++)
        {
             int current = result[i-j*j]+1;

             if(current < result[i])
             {
                result[i] = current;

             }
        }
    }

    return result[n];
}
