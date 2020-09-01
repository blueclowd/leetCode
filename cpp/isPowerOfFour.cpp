#include <iostream>

using namespace std;

class IsPowerOfFour
{
    public:

        bool isPowerOfFour(int num)
        {
            // Two criterions:
            // 1. only one 1 in the bitwise presentation
            // 2. 1 should be located at the odd digits
            return (num & (num-1)) == 0 && (num & 0x55555555);
        }
};

int main(void)
{
    IsPowerOfFour isPowerOfFour;

    cout<<isPowerOfFour.isPowerOfFour(4)<<endl;
}
