#include<stdio.h>
#include<string.h>
void replace(char s[], int pos,char corWord[]){
    int i,end;
    
    for(i = pos; i < strlen(s); i++){
        if (s[i] == ' '){
            end = i-1;
            break;
        }
    }
    // printf("%d %d", pos, end);
    for(i = 0; i < strlen(s); i++){
        if (i == pos){
            printf("%s",corWord);
            i = end;
        } else {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}

void main(){
    char s[1000], corWord[50];
    int pos;

    printf("Enter your sentence: ");
    gets(s);
    printf("Enter position of wrong word: ");
    scanf("%d", &pos);
    printf("Enter correct word: ");
    scanf("%s", &corWord);
    replace(s,pos,corWord);
}