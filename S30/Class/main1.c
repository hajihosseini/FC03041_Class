#include<stdio.h>

struct Student
{
    int id;
    char name[10];
    int ssn;
    int credits;
};

void copys(char* pchDst, char* pchSrc)
{
    while(*pchSrc)
    {
        *pchDst = *pchSrc;
        pchSrc++;
        pchDst++;        
    }
    *pchDst = 0;
}
void main()
{
    // int nums[3] = {1,2,3};
    struct  Student s;
    s.id = 0x88ffaabb;
    s.ssn = 0x11111111;
    s.credits = 17;
    copys(s.name, "AABBAABBA");
    printf("%x, %x, %d, %s\n", s.id, s.ssn, s.credits, s.name);
    copys(s.name, "AABBAABBA shirazi");
    printf("%x, %x, %d, %s\n", s.id, s.ssn, s.credits, s.name);
    s.ssn = 0x11111111;
    printf("%x, %x, %d, %s\n", s.id, s.ssn, s.credits, s.name);
}