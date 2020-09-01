
/**
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/
int factorial(int,int);

int climbStairs(int n)
{

    double numWay = 0;
    int idx = 0;
    int oneStep = n, twoStep = 0;

    while( oneStep >= 0)
    {

        printf("1 = %d, 2 = %d \n", oneStep, twoStep);

        numWay += factorial(oneStep, twoStep);

        idx++;
        oneStep = n - 2*idx;
        twoStep = idx;

    }

    printf("%.20f \n", numWay);
    printf("%d \n", (int)numWay);

    return (int)numWay;
}

int factorial(int a, int b)
{
    double product = 1;
    int smaller = a > b ? b : a;

    int numerator = a+b;
    int denominator = smaller;

    int cnt;
    for(cnt = 0; cnt<smaller; ++cnt)
    {
        product *= (numerator--);

        product /= (denominator--);
    }

    return round(product);

}
