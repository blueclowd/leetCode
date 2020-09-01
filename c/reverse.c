#include <limits.h>
/**
Reverse digits of an integer.
*/
int reverse(int x)
{

    printf("Input: %d \n", x);

    // Record the sign of the number
    const int sign = x < 0 ? -1 : 1;

    // Take the value for reverse
    x = abs(x);

    int reverseNum = 0;

    int digit = 0;

    while(x)
    {
        digit = x % 10;
        x /= 10;

        // Check overflow
        if (reverseNum > (INT_MAX / 10))
        {
            return 0;
        }

        // Check overflow
        if ((reverseNum *= 10) > (INT_MAX - digit))
        {
            return 0;
        }
        reverseNum  += digit;

    }

    printf("Reverse = %d ", reverseNum* sign);

    return reverseNum * sign;
}
