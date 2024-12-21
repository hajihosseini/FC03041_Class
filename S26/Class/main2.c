#include<stdio.h>

void main()
{
    int x = 5;
    int y = 6; 
    int z = 7;
    int nums[10] = {1,2,3,4,5,6,7,8,9,10};
    int sum = 0;
    for(int i=0; i<10; i++)
    {        
        sum += nums[i];
        printf("%d,", nums[i]);
    }
    
    printf("\n%d\n", sum);
    printf("\n%p, %d\n", nums, sizeof(nums));
}