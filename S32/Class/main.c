#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma pack(push, 1)
typedef struct _Student
{
    int id;
    char name[20];
    int ssn;
    int credits;
} Student;
#pragma pack(pop)

void Usage()
{
    printf("main.exe list\n");
    printf("main.exe reg <stdid> <name> <ssn> <credits>\n");
}

int mystrcmp(char* pch1, char* pch2)
{
    while (*pch1 && *pch2)
    {
        if (*pch1 != *pch2)
            return 0;
        pch1++;
        pch2++;
    }
    return *pch1 == *pch2;
}

void print_list()
{
    FILE* pf = fopen("students.txt", "r");
    Student s;
    memset(&s, 0, sizeof(Student));
    while(1)
    {
        int rv = fscanf(pf, "%d\n", &(s.id));
        if (rv == EOF)
            break;
        fscanf(pf, "%s\n", &(s.name));
        fscanf(pf, "%d\n", &(s.ssn));
        fscanf(pf, "%d\n", &(s.credits));
        printf("%d\n%s\n%d\n%d\n", s.id, s.name, s.ssn, s.credits);
    }

}

void copys(char* pSrc, char* pDst)
{
    while(*pSrc)
    {
        *pDst = *pSrc;
        pSrc++;
        pDst++;
    }
    *pDst = *pSrc;
}

void register_student(char** params)
{
    char* id = params[0];
    char* name = params[1];
    char* ssn = params[2];
    char* credits = params[3];
    Student* ps = malloc(sizeof(Student));
    memset(ps, 0, sizeof(Student));
    ps->id = atoi(id);
    copys(name, ps->name);
    ps->ssn = atoi(ssn);
    ps->credits = atoi(credits);

    FILE* pf = fopen("students.txt", "a+");
    fprintf(pf, "%d\n%s\n%d\n%d\n", ps->id, ps->name, ps->ssn, ps->credits);
    fclose(pf);
}


    // int n = 0;
    // ps->id = *((int*) id);
    // memset(&n, 0, sizeof(int));
    // printf("%s\n%s\n%s\n%s", id, name, ssn, credits);

int main(int argc, char** argv)
{


    if ((argc == 2 ) && mystrcmp(argv[1],"list"))
    {
        print_list();
    }
    else 
    if ((argc == 6) && mystrcmp(argv[1], "reg"))
    {
        register_student(argv+2);
    }
    else
    {
        Usage();
        return -1;
    }

    return 0;
}