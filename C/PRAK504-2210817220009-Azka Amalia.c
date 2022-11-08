#include<stdio.h>
int reverse(int num){
    int n=0, rem;
   while(num){
        rem=num%10;
        n=n*10+rem;
        num=num/10;}
        return n;
}
int main(){
    int A, B;
    scanf("%d%d",&A,&B);
    A=reverse(A);
    B=reverse(B);
    int C = A+B;
    printf("%d",reverse(C));
}
