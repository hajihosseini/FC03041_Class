#include<stdio.h>

int add(int a, int b)
{
    int result = a + b;
    return result;
}

int averagei(float a, float b)
{
    return (a+b)/2;
}


float average(float a, float b)
{
    printf("this is the average function and the input is %f and %f ", a, b);
    float result = (a+b)/2;
    printf("the result is also %f", result);
    return (a+b)/2;
}

void print_my_name()
{
    printf("my name is Ali\n");
}

void main()
{
    int ww = 128;
    char d = 127;
    printf("%d\n", d);
    d--; 
    printf("%d\n", d);
    while (d)
    {
        d--;
        printf("%d, %x, %c\n", d, d, d);
    }



    // printf("size of float is %d\n", sizeof(float));
    // printf("size of int is %d\n", sizeof(int));
    // printf("size of double is %d\n", sizeof(double));
    // printf("size of char is %d\n", sizeof(char));
    // printf("size of long is %d\n", sizeof(long));
    // printf("size of long long int is %d\n", sizeof(long long int));






    // int c;
    // printf("%d\n", c);
    // c = add(5, 4);
    // float r = averagei(1.2, 5.3);
    // printf("averagei = %f\n", r);
    // r += 1;
    // printf("%d\n", c);
    // int w, x, z, y, n;
    // printf("%d,\n %d,\n %d, %d, %d\n", w, x, z, y, n);
}