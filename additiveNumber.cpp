#include <string>
#include <cstdlib>
#include <iostream>
#include <sstream>

using namespace std;

class Solution
{
    public:
        // Main method: check if string is an additive number
        bool isAdditiveNumber(string num)
        {
            if (num.size()<3)
            {
                return false;
            }

            for (int i = 1; i < num.size()-1; i++)
            {
                for (int j = 1; j < num.size()-1;j++)
                {

                    if (helper(num.substr(0,i), num.substr(i,j), num, i+j))
                    {
                        return true;
                    }
                }
            }

            return false;
        }

    private:

        // Given two strings, check if there exists accurate sum in the succesive character sequence
        bool helper(string pre1, string pre2, string& num, int start)
        {
            cout << pre1 <<","<< pre2 << "," << num << "," << start << endl;

            if (checkLeadingZero(pre1) || checkLeadingZero(pre2) )
            {
                return false;
            }

            for (int i = 0; start+i < num.size();i++)
            {
                string sum = num.substr(start, i+1);

                if (checkLeadingZero(sum))
                {
                    return false;
                }

                if (myStol(sum) == myStol(pre1) + myStol(pre2))
                {

                    if (start + i == num.size()-1)
                    {
                        return true;
                    }

                    if (helper(pre2, sum, num, start+i+1))
                    {
                        return true;
                    }

                }
            }

            return false;
        }

    private:
        // Convert from string to long
        long myStol(string s)
        {
            stringstream ss(s);
            long result;
            ss >> result;
            return result;
        }

    private:
        // Check if string has leading zero (excluding zero)
        bool checkLeadingZero(string s)
        {
            return (s.size() > 1) && (s[0] == '0');
        }

};

int main(void)
{
    Solution solution;
    cout<< "Is additive = " << solution.isAdditiveNumber("123") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("303") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("011") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("12358") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("199100199") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("1991200") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("1023") << endl;
    cout<< "Is additive = " << solution.isAdditiveNumber("1203") << endl;
}
