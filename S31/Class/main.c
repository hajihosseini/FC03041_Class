#include<stdio.h>

#pragma pack(push,1)
typedef struct _Student
{
    int id;
    char name[10];
    int ssn;
    int credits;
} Student;
#pragma pack(pop)

void print_student1(Student s)
{
    printf("id: %d\n", s.id);
    printf("ssn: %d\n", s.ssn);
    printf("credits: %d\n", s.credits);
    printf("name: %s\n", s.name);
}

void print_student(Student* s)
{
    printf("id: %d\n", s->id);
    printf("ssn: %d\n", s->ssn);
    printf("credits: %d\n", s->credits);
    printf("name: %s\n", s->name);
}

void main()
{
    Student s[2] = {{
        .id = 0x88aaff11,
        .name = "Zari",
        .ssn = 0x88aa8811,
        .credits = 8
    },
    {
        .id = 0x88aaff11,
        .name = "Zari",
        .ssn = 0x88aa8811,
        .credits = 8
    }};

    Student s1 = {
        .id = 0x88aaff11,
        .name = "Pari",
        .ssn = 0x88aa8811,
        .credits = 8
    };

    Student s2 = {
        .id = 0x88aaff11,
        .name = "Mari",
        .ssn = 0x88aa8811,
        .credits = 8
    };

    int nums[3] = {1, 2, 3}; int x = 5;
    Student stdlist[3] = {
        {
            .id = 0x88aaff11,
            .name = "Zari",
            .ssn = 0x88aa8811,
            .credits = 8
        },
        {
            .id = 0x88aaff11,
            .name = "Pari",
            .ssn = 0x88aa8811,
            .credits = 8
        },
        {
            .id = 0x88aaff11,
            .name = "Mari",
            .ssn = 0x88aa8811,
            .credits = 8
        }
    };

    Student* students[4] = {&s1, &s2, s, stdlist};
    int xxid = students[3][1].id;

    int matrix[3][2] = {
        {0x11, 0x22},
        {0xaa, 0xbb},
        {0xcc, 0xdd}
    };

    int pn1[2] = {0x11, 0x22};
    int pn2[2] = {0xaa, 0xbb};
    int pn3[2] = {0xcc, 0xdd};
    int* jagged_array[3] = {pn1, pn2, pn3};

    stdlist[0].id;
    students[0]->id;
    printf("%x", stdlist[0]);

    // print_student(&s);


    // struct Student * ps = &s;
    // char* pch = (char*) ps;

    // int* pn = (int*) (pch+14);
    // int* pnt = &(s.ssn);
    // printf("%x\n", *pn);
    // printf("%x\n", *(pch+14));
    // printf("%p\n%p\n", pn, pnt);


    // printf("%c\n", *(pch+6));
    // printf("%s\n", pch+4);
    // printf("%s\n", s.name);
    // printf("%s\n", pch+9);
}