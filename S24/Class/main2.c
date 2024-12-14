#include<stdio.h>


unsigned char revbits(unsigned char b)
{

}

unsigned char setbit(unsigned char ch, int i)
{
    return (1 << i) | ch;
}

void main()
{
    unsigned char ch = 'A';
    unsigned char bh = setbit(ch, 1);
    printf("%c\n", bh);
}

void main2()
{
    unsigned char ch = 'A';
    unsigned char b = 0x80;
    for (int i=0; i<sizeof(ch)*8; i++)
    {
        char x = ch & b;
        if (x != 0)
        {
            x = 1;
        }
        printf("%d ", x);
        b = b >> 1;
    }
    printf("\n");
}