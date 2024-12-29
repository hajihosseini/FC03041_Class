#include<stdio.h>

void swap(int* a, int* b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void main()
{
    int w = 5;
    int* x = NULL;
    // if (x !=  NULL)
    {
        *x = 5;
    }
    printf("done\n");

}


void main2()
{
    int x = 5;
    int y = 6;
    printf("%d, %d\n", x, y);
    swap(&x, &y);
    printf("%d, %d\n", x, y);
}