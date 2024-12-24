#include<stdio.h>
void f3(int* y)
{
    printf("f3:%p, %d\n",y, *y);
    (*y)++;
    printf("f3:%p, %d\n",y, *y);
}
void f2(int* x)
{
    (*x)++;
    printf("f2:%p, %d\n", x, *x);
    f3(x);
    printf("f2:%p, %d\n", x, *x);
}
void f1(int* w)
{
    (*w)++;
    printf("f1:%p, %d\n", w, *w);
    f2(w);
    printf("f1:%p, %d\n", w, *w);
}
void main()
{
    int x = 5;
    printf("main:%p, %d\n", &x, x);
    f1(&x);
    printf("main:%p, %d\n", &x, x);
}