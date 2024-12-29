#include "memory.h"
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "doctest.h"

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

    TEST_CASE("byte of integer")
    {
        unsigned int n = 0xffaaeedd;
        unsigned char first_byte = 0xdd;
        unsigned char second_byte = 0xee;
        unsigned char third_byte = 0xaa;
        unsigned char forth_byte = 0xff;

        CHECK(first_byte == get_byte(n, 0));
        CHECK(second_byte == get_byte(n, 1));
        CHECK(third_byte == get_byte(n, 2));
        CHECK(forth_byte == get_byte(n, 3));
    }

    // TEST_CASE("pointer math")
    // {
    //     char pch[15] = "abcdefghijkl";
    //     char *actual = address_plus(&(pch[2]), 4);
    //     char *expected = &(pch[6]);
    //     CHECK(actual == expected);

    //     actual = address_plus(&(pch[1]), 7);
    //     expected = &(pch[8]);
    //     CHECK(actual == expected);
    // }

    // TEST_CASE("array as integer")
    // {
    //     char pch[5] = "AAAA";
    //     int actual = array_as_int(pch);
    //     int expected = 0x41414141;
    //     CHECK(actual == expected);

    //     char pch2[4] = "BBB";
    //     actual = array_as_int(pch2);
    //     expected = 0x00424242;
    //     CHECK(actual == expected);

    //     pch[0] = 0;
    //     actual = array_as_int(pch);
    //     expected = 0x41414100;
    //     CHECK(actual == expected);
    // }
}