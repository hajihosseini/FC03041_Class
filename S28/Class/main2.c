#include<stdio.h>
int f3(int y)
{
    printf("f3: %d\n", y);
    y++;
    printf("f3: %d\n", y);
    return y;
}
int f2(int x)
{
    x++;
    printf("f2: %d\n", x);
    x = f3(x);
    printf("f2: %d\n", x);
    return x;
}
int f1(int w)
{
    w++;
    printf("f1: %d\n", w);
    w = f2(w);
    printf("f1: %d\n", w);
    return w;
}
void main()
{
    int x = 5;
    printf("main: %d\n", x);
    x = f1(x);
    printf("main: %d\n", x);
}