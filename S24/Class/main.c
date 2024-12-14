#include<stdio.h>

void main()
{
    char ch = 'A';
    for (int i=0; i<sizeof(ch)*8; i++)
    {
        char x = ch & 0x80;
        if (x != 0)
        {
            x = 1;
        }
        printf("%d ", x);
        ch = ch << 1;
    }
    printf("\n");
}