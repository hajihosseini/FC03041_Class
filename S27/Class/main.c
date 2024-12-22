#include<stdio.h>

void print_nums2(int* pn, int size)
{
    while(size--)
        printf("%d,", *(pn++));
    printf("\n");
}
void print_nums(int* pn, int size)
{
    for(int i=0; i<size; i++)
        printf("%d,", pn[i]);
    printf("\n");
}

void reverse_nums(int*pn, int size)
{
    for(int i=0; i<((size+1)/2); i++)
    {
        int t = pn[i];
        pn[i] = pn[size-1-i];
        pn[size-1-i] = t;
    }
}

void main()
{
    int nums[6] = {1, 2, 3, 4, 5, 6};
    print_nums(nums, 4);
    reverse_nums(nums, 4);
    print_nums(nums, 4);

}

void main3()
{
    int nums[6] = {0xaaff, 0xffee, 0x11ff, 0xaaff, 0xffff, 0xaaaa};
    
    for(
        int* pn = &(nums[0]); 
        pn < (&(nums[0]) + 6); 
        pn++)
    {
        printf("%x,", *pn);
    }
    // for(int i=0; i<6; i++)
    //     printf("%x,", nums[i]);
    printf("\n");
}

void main2()
{
    int x;
    x = 4;
    x = x + 1;
    int nums[6] = {0xaaff, 0xffee, 0x11ff, 0xaaff, 0xffff, 0xaaaa};
    int w = nums[0];
    nums[5] = w + 1;
    printf("%p\n%p\n%llu\n%llu\n%llx\n%llx\n", 
        &(nums[0]), &(nums[5]),
        &(nums[0]), &(nums[5]),
        &(nums[0]), &(nums[5]));

    // int pn5 = (int) &(nums[5]);
    // int pn0 = (int) &(nums[0]);

    printf("%p\n", &(nums[5])-&(nums[0]));
    // printf("%d\n", pn5-pn0);
    
    char buf[6] = {'a', 'b', 'c', 'd', 'e', 'f'};
    char buf1[6] = {1,2,3,4,5,6};
    printf("%p\n", &(buf[5])-&(buf[0]));
}