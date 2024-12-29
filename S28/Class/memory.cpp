#include <stdio.h>
#include "memory.h"
#define CHECK(cnd)           \
    if (cnd)                 \
    {                        \
        printf("success\n"); \
    }                        \
    else                     \
    {                        \
        printf("failed\n");  \
    }

#define TEST_SUITE(pp) printf("%s\n", pp);
#define TEST_CASE(pp) TEST_SUITE(pp)
#define SUBCASE(pp) TEST_SUITE(pp)

int main()
{
    TEST_SUITE("memory")
    {
        TEST_CASE("variable swap")
        {
            int a = 5;
            int b = 10;
            swap(&a, &b);
            CHECK(a == 10);
            CHECK(b == 5);

            a = 5;
            b = 10;

            SUBCASE("first NULL pointer")
            {
                swap(&a, nullptr);
                CHECK(a == 5);
            }

            SUBCASE("second NULL pointer")
            {
                swap(nullptr, &b);
                CHECK(b == 10);
            }

            SUBCASE("second NULL pointer")
            {
                swap(nullptr, nullptr);
            }
        }
    }
}

// int main3(int argc, char const *argv[])
// {
//     int a = 5;
//     int b = 6;
//     swap(&a, &b);
//     printf("%d, %d", a, b);
//     /* code */
//     return 0;
// }
