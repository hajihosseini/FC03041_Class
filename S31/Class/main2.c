#include<stdio.h>
#include<stdlib.h>

#pragma pack(push,1)
typedef struct _Student
{
    int id;
    char name[10];
    int ssn;
    int credits;
} Student;
#pragma pack(pop)

int last_id = 4035210;
void copys(char* pSrc, char*pDst)
{
    while(*pSrc)
    {
        *pDst = *pSrc;
        pSrc++;
        pDst++;
    }
    *pDst = 0;
}

Student* make_student(char** name, int count)
{
    Student* ps = malloc(sizeof(Student)*4);
    for(int i=0; i<count; i++)
    {
        ps->id = ++last_id;
        copys(name, ps->name);
        ps->credits = 17;
        ps->ssn = 0;
    }
    return ps;
}

void print_student(Student* s)
{
    printf("id: %d\n", s->id);
    printf("ssn: %d\n", s->ssn);
    printf("credits: %d\n", s->credits);
    printf("name: %s\n", s->name);
}

Student* register_all_students()
{
    char* names[]  = {"Ali", "Zari", "Pari", "Mari"};
    // char names[]  = "Ali";
    Student* s = make_student(names, 4);
    return s;
}

void main()
{
    Student* s = register_all_students();
    print_student(s);
}