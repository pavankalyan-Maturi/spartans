/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
int main()
{
    int a[5]={1,2,3,4,5},i=0;
    int *ptr,sum=0;
    ptr=a;
    for(i=0;i<5;i++)
    {
       sum=sum+*ptr;
       ptr++;
       
    }
    printf("%d",sum);

    return 0;
}
