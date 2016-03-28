#include <stdbool.h>
/**
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
*/
bool isHappy(int n) {

    while(n != 1)
    {
        int n = sumOfSquares(n);

        if (n == 4)
        {
            return false;
        }
    }

    return true;
}

/**
Calculate the sum of squares of digits
*/
int sumOfSquares(int n)
{
    int sum = 0;
    while(n)
    {
        int remain = n % 10;

        sum += remain*remain;

        n = n/10;
    }

    return sum;
}
