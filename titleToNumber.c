
/**
Given a column title as appear in an Excel sheet, return its corresponding column number.
*/
int titleToNumber(char* s) {

    const int digitNum = strlen(s);

    int number = 0;
    int i;
    for (i = 0 ; i < digitNum ; ++i)
    {
        number *= 26;
        number += (s[i] - 64);
    }

    printf("Number = %d \n", number);

    return number;
}
