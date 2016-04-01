
/**
Follow up for H-Index: What if the citations array is sorted in ascending order?
Could you optimize your algorithm?
*/
int hIndex(int* citations, int citationsSize)
{
    int start = 0;
    int end = citationsSize-1;
    int mid;
    int hIndex;
    int okHIndex = 0;

    while (start <= end)
    {
        mid = start + (end-start)/2;
        hIndex = citationsSize - mid;

        if (citations[mid] >= hIndex && citations[mid-1] <= hIndex)
        {
            okHIndex = hIndex;

            start = mid+1;
        }
        else if (citations[mid] < hIndex)
        {
            start = mid+1;
        }
        else
        {
            end = mid-1;
        }

    }

    return okHIndex;

}
