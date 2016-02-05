#include <math.h>

/**
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
*/
int trailingZeroes(int n) {

    printf("Input: %d\n",n);

    int exp;
    double k = log10(n)/log10(5);

    int count = 0;

    for (exp = 1; exp <= k; ++exp)
    {
        count += floor(n/pow(5,exp));
    }

    printf("Output: %d\n", count);

    return count;

}
