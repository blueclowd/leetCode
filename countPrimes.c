#include <stdbool.h>
#include <math.h>
/**
Count the number of prime numbers less than a non-negative number, n.
*/
int countPrimes(int n) {

    bool *isComposite = (int*)malloc(sizeof(int)*n);

    int idx;
    int count = 0;

    // Check each number started from 2
    for (idx = 2; idx < n;idx++)
    {
        if (!isComposite[idx])
        {
            count++;

            int j;
            for(j = idx; j < n;j+=idx)
            {
                isComposite[j] = true;
            }
        }
    }

    return count;
}
