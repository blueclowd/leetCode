#include <stdlib.h>

/**
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each,
and the other N − h papers have no more than h citations each."
*/
int cmp(const void* a, const void* b);

int hIndex(int* citations, int citationsSize) {

    qsort(citations, citationsSize, sizeof(int), cmp);

    if (citationsSize == 1 && *citations == 0)
    {
        return 0;
    }

    int i;
    int hIndex = 0;
    for(i = 1;i <= citationsSize;i++)
    {
        if (citations[citationsSize-i] >= i)
        {
            if (citationsSize-i-1 < 0 || citations[citationsSize-i-1] <= i)
            {
                hIndex = i;
            }
        }
    }

    printf("HIndex = %d", hIndex);

    return hIndex;
}

int cmp(const void* a, const void* b)
{
    return *(int*)a - *(int*)b;
}
