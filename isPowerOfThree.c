#include <limits.h>
/**
Given an integer, write a function to determine if it is a power of three.
*/
int isPowerOfThree(int n)
{
    if(n<1)
    {
        return 0;
    }

    const int max3Exp = log10(INT_MAX)/log10(3);

    const int max3Power = pow(3, max3Exp);

    return max3Power % n ==0;
}
