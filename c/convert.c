char* convert(char* s, int numRows) {

    int row;
    int length = strlen(s);

    char *result = (char*)malloc(sizeof(char)*length);

    if (numRows <=1)
    {
        return s;
    }

    int index = 0;

    for(row = 0; row < numRows; row++)
    {
        int dist = row;
        int prev = -1;
        int flag = -1;

        while(dist < length)
        {

            if (dist != prev)
            {
                result[index++] = s[dist];
                prev = dist;
            }

            if (flag == -1)
            {
                dist += 2*(numRows-(row+1));
            }
            else
            {
                dist += 2*row;
            }

            flag *= -1;

        }
    }

    return result;
}
