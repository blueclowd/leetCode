#include <stdint.h>

/**
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).
*/
uint32_t reverseBits(uint32_t n)
{
    printf("Input: %d \n", n);

    int idx;
    uint32_t result = 0;

    for (idx = 0; idx < 32; idx++)
    {
        // Get the bit in position idx and shift to position 31-idx
        result += ((n >> idx) & 1) << (31-idx);
    }

    printf("Output: %d \n", result);

    return result;
}
