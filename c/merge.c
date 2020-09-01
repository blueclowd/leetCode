/**
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
*/
void merge(int* nums1, int m, int* nums2, int n)
{

    printf("Input: m = %d , n = %d \n", m,n);
    int idx1 = 0, idx2 = 0;

    int* mergeAry = (int*)malloc((m+n)*sizeof(int));

    int mergeIdx = 0;
    while(idx1<m & idx2<n)
    {
        // Compare each pair of elements, push the smaller one into mergeAry
        if (nums1[idx1] < nums2[idx2])
        {
            mergeAry[mergeIdx++] = nums1[idx1++];
        }
        else
        {
            mergeAry[mergeIdx++] = nums2[idx2++];
        }
    }

    // Push remaining elements in nums1 or nums2
    while(idx1<m)
    {
        mergeAry[mergeIdx++] = nums1[idx1++];
    }

    while(idx2<n)
    {
        mergeAry[mergeIdx++] = nums2[idx2++];
    }

    // Rewrite into nums1 and print
    for (mergeIdx = 0; mergeIdx<m+n; mergeIdx++)
    {
        nums1[mergeIdx] = mergeAry[mergeIdx];

        printf("%d ", nums1[mergeIdx]);
    }
}
