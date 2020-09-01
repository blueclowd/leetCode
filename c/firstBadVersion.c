#include <stdbool.h>

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n)
{
    int start = 1;
    int end = n;
    int middle = 1 + (n-1)/2;

    while(start != end)
    {

        bool isBad = isBadVersion(middle);

        if (isBad)
        {
            end = middle;
        }
        else
        {
            start = middle+1;
        }

        middle = start+(end-start)/2;

    }

    return middle;
}
