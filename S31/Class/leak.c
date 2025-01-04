#include<stdio.h>
#include<stdlib.h>
#include<windows.h>


void main()
{
    for(int i=0; i<100000000; i++)
    {
        int* p = malloc(1500*1024);
        printf(".");
        Sleep(10);
        free(p);
    }
}