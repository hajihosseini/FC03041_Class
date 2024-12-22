#include<stdio.h>


void t()
{
    char pch[10] = "abcdefghi";
    char pch1[10] = "abcdefghi";
    char pch2[10] = "abcdefghi";
}

int slen2(char* pch)
{
    int i;
    for(i=0; pch[i] != 0; i++)
        ;
    return i;
}

char* get_buf()
{
    char buf[10] = "ali";
    return buf;
}

void get_buf2(char* buf, int size)
{
    buf[0] = 'a';
    buf[1] = 'z';
    buf[2] = 0;
}

void append(char* str1, char* str2, char* str3)
{

}

int slen(char* pch)
{
    int count = 0;
    while (*(pch++) != 0)
        count++;
    return count;
}

void main()
{
    char str1[10] = "ali";
    char str2[10] = "azar";
    char ezdevaj[20];
    append(str1, str2, ezdevaj);
}

void main4()
{
    char str[12] = "azar ali";
    printf("%d\n", slen(str));
    printf("%s\n", str);
    str[4] = '0';
    printf("%d\n", slen(str));
    printf("%s\n", str);
    str[6] = ' ';
    printf("%s\n", str+5);

}

void main2()
{
    int x = 0xaaffaaff, y = 0xaaffaaff, z = 0xaaffaaff;
    t();
    char str1[10];
    char str[10];
    str[0] = 'A';
    str[1] = 'z' ;
    str[2] = 'a' ;
    str[3] = 'r' ;
    str[4] = 0 ;
    str[6] = 's' ;
    str[7] = 's' ;
    printf("%s\n", str);
    printf("%c", str[9]);
}