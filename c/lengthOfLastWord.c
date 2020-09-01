#include <stdlib.h>
#include <string.h>

/**
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
*/
int lengthOfLastWord(char* s) {

    if (s == NULL || strlen(s) == 0)
    {
        return 0;
    }

    char *tokens = strtok(s," ");

    char *currentToken = tokens;

    while(tokens != NULL)
    {
        currentToken = tokens;

        printf("%s \n", currentToken);

        tokens = strtok(NULL," ");
    }

    return currentToken == NULL ? 0 : strlen(currentToken);
}
