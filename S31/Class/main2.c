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


Student* make_student(char* name)
{
    Student* ps = malloc(sizeof(Student));
    ps->id = ++last_id;
    copys(name, ps->name);
    ps->credits = 17;
    ps->ssn = 0;
    return ps;
}

void print_student(Student** pps, int count)
{
    for(int i=0; i<count; i++)
    {
        printf("id: %d\n", pps[i]->id);
        printf("ssn: %d\n", pps[i]->ssn);
        printf("credits: %d\n", pps[i]->credits);
        printf("name: %s\n", pps[i]->name);
    }
}

void print_student2(Student** pps, int count)
{
    while(count--)
    {
        printf("id: %d\n", (*pps)->id);
        printf("ssn: %d\n", (**pps).ssn);
        printf("credits: %d\n", (*pps)->credits);
        printf("name: %s\n", (*pps)->name);
        pps++;
    }
}

void t()
{
    char buf[255] = "asdlfjals;dkjfla;skdjf;laskdjf;laksdjf;laksjdf;laskjdfla";
    int n  = 5;
    int *pn = &n;

    int *x = pn;
}

int register_all_students(Student *** ps)
{
    char* names[]  = {"Ali", "Zari", "Pari", "Mari"};
    Student** pss = malloc(sizeof(Student*)*4);
    for(int i=0; i<4; i++)
         pss[i] = make_student(names[i]);
    *ps = pss;
    return 4;
}
void free_resources(Student** pps, int count)
{
    for(int i=0; i<count; i++)
        free(pps[i]);
    free(pps);
    printf("done.\n");
}
void main()
{
    Student** ps = NULL;
    int count = register_all_students(&ps);
    t();
    print_student(ps, count);
    free_resources(ps, count);
}