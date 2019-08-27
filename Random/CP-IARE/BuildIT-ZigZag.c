#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    //Write your code here
    int n, i, j, temp, strl;
    char s[1000];
    gets(s);
    strl = strlen(s);
    char arr[strl][strl];
    scanf("%d", &n);
    for(i = 0; i < strl; i++){
        for(j = 0; j < strl; j++){
            arr[i][j] = "\n";
        }
    }

    printf(arr[1][1]);


}