#include<stdio.h>
int ds(int n){//sas
    int sd=0;
    while(n>0){//for summing the digits
        sd=sd+(n%10);
        n=n/10;
    }
    return sd;//sd is the sum 
}
int main(){
    int n;
    scanf("%d",&n);//input
    while(n>9){
        n=ds(n);//calling function
    }
    printf("%d is generic root\n",n);//output statement
    return 0;
}
