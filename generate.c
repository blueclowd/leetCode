
/**
Given numRows, generate the first numRows of Pascal's triangle.
*/
int** generate(int numRows, int** columnSizes, int* returnSize) {

    printf("%d \n", numRows);

    *returnSize = numRows;

    printf("%d \n", numRows);


    int **result = (int**)malloc(sizeof(int*)*numRows);
    *columnSizes = (int*)malloc(sizeof(int) * numRows);

    printf("%d \n", numRows);

    int row;
    for(row = 0; row < numRows; row++)
    {
        result[row] = (int*)malloc(sizeof(int)*(row+1));
        (*columnSizes)[row] = row+1;

        int col;
        for(col = 0;col < row;col++)
        {
            if (col == 1 || col == row)
            {
                result[row][col] = 1;
            }
            else
            {
                result[row][col] = result[row-1][col] + result[row-1][col-1];
            }
        }

    }

    return result;

}
