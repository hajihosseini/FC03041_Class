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

// Student* make_student(char** name, int count)
// {
//     Student* pso = malloc(sizeof(Student)*count);
//     Student* ps = pso;
//     for(int i=0; i<count; i++)
//     {
//         ps->id = ++last_id;
//         copys(name, ps->name);
//         ps->credits = 17;
//         ps->ssn = 0;
//         ps++;
//     }
//     return pso;
// }


Student* make_student(char** name, int count)
{
    Student* ps = malloc(sizeof(Student)*count);
    for(int i=0; i<count; i++)
    {
        ps[i].id = ++last_id;
        copys(name[i], ps[i].name);
        ps[i].credits = 17;
        ps[i].ssn = 0;
    }
    return ps;
}

void print_student(Student* s, int count)
{
    while(count--)
    {
        printf("id: %d\n", s->id);
        printf("ssn: %d\n", s->ssn);
        printf("credits: %d\n", s->credits);
        printf("name: %s\n", s->name);
        s++;
    }
}

void print_student1(Student* s, int count)
{
    for(int i=0; i<count; i++)
    {
        printf("id: %d\n", s[i].id);
        printf("ssn: %d\n", s[i].ssn);
        printf("credits: %d\n", s[i].credits);
        printf("name: %s\n", s[i].name);
    }
}

int register_all_students(Student ** ps)
{
    char* names[]  = {"Ali", "Zari", "Pari", "Mari"};
    // char names[]  = "Ali";
    *ps = make_student(names, 4);
    return 4;
}

void main()
{
    Student* ps = NULL;
    int count = register_all_students(&ps);
    print_student(ps, count);
}