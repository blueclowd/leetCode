
/**
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
*/
int isCarry(int*, int);

int* plusOne(int* digits, int digitsSize, int* returnSize)
{

    // Default carry = 1: plus one
    int carry = 1;

    // Determine returnSize: digitSize+1 if all digits are 9
    *returnSize = isCarry(digits, digitsSize) ? digitsSize+1 : digitsSize;

    int *result = (int*)malloc((*returnSize)*sizeof(int));

    int returnIdx = *returnSize - 1;

    int i;
    for (i = digitsSize -1 ; i >= 0; i--)
    {
        int tmpResult = digits[i] + carry;

        carry = tmpResult / 10;

        result[returnIdx--] = tmpResult % 10;
    }

    result[returnIdx] = carry;

    return result;
}

int isCarry(int *num, int digitsSize)
{
    int i;
    for(i = 0;i<digitsSize; ++i)
    {
        if (num[i] != 9)
        {
            return 0;
        }
    }

    // The number carries if all digits are 9
    return 1;
}
