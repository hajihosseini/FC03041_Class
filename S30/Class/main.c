#include<stdio.h>
void print2d(int** nums2d, int* lens, int len)
{
    for(int i=0; i<len; i++)
        for(int j=0; j<lens[i]; j++)
            printf("[%d,%d] = %d\n", i, j, nums2d[i][j]);
}


void main1()
{
    int nums1[3] = {1, 2, 3}; 
    int nums2[2] = {3, 2}; 
    int nums3[5] = {3, 2, 1, 0, -1}; 
    int lens[3] = {3, 2, 5};
    // int* pn = nums;
    int* nums2d[3] = {nums1, nums2, nums3};
    print2d(nums2d, lens, 3);

    // for(int i=0; i<2; i++)
    //     for(int j=0; j<lens[i]; j++)
    //         printf("[%d,%d] = %d\n", i, j, nums2d[i][j]);
}


void print_args1(int argc, char** argv)
{
    for(int i=0; i<argc; i++) {
        printf("%s\n", argv[i]);
    }
}

void print_args(int argc, char** argv)
{
    for(int i=0; i<argc; i++) {
        for(int j=0; argv[i][j] != 0; j++)
            printf("%c",argv[i][j]);
        printf("\n");
    }
}

int main(int argc, char**argv)
{    
    print_args(argc, argv);
    int n;
    scanf("%d", &n);
    printf("\nyou entered %d", n);
}