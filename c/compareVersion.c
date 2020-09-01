#include <string.h>

/**
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

*/
int compareVersion(char* version1, char* version2)
{

    char* rest1 =NULL;
    char* rest2 =NULL;

    char *token1 = strtok_r(version1, ".", &rest1);
    char *token2 = strtok_r(version2, ".", &rest2);

    int result = 0;
    while(token1 != NULL | token2 != NULL)
    {
        result = compareToken(token1, token2);

        if (result != 0)
        {
            return result;
        }
        else
        {
            token1 = strtok_r(rest1, ".", &rest1);
            token2 = strtok_r(rest2, ".", &rest2);
        }
    }

    return result;

}

int compareToken(char* token1, char* token2)
{

    token1 = token1 == NULL ? "0": token1;
    token2 = token2 == NULL ? "0": token2;

    int result = -2;

    if(atoi(token1) > atoi(token2))
    {
        result = 1;
    }
    else if(atoi(token1) < atoi(token2))
    {
        result = -1;
    }
    else
    {
        result = 0;
    }

    return result;
}


