#include <stdbool.h>

bool isPalindrome(int x) {

    if (x < 0)
    {
        return false;
    }

    int reverse = 0;
    int orig = x;

    while(orig!=0)
    {
        reverse *= 10;
        reverse += orig % 10;

        orig /=10;
    }

    printf("%d \n", reverse);

    return x == reverse;
}
