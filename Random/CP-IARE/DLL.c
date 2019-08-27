#include<stdio.h>
struct node{
    int data;
    struct node *ll, *rl;
};

struct node* insertL(int data, struct node *Rh){

    struct node *n = (struct node*)malloc(sizeof(struct node));
    n->data = data;
    n->rl = NULL;
    n->ll = NULL;
    if(Rh == NULL){
        Rh = n;
        return Rh;
    }
    n->ll = Rh;
    Rh->rl = n;
    Rh = n;
    return Rh;
}

struct node* insertF(int data, struct node *Lh){

    struct node *n = (struct node*)malloc(sizeof(struct node));
    n->data = data;
    n->rl = NULL;
    n->ll = NULL;
    if(Lh == NULL){
        Lh = n;
        return Lh;
    }
    n->rl = Lh;
    Lh->ll = n;
    Lh = n;
    return Lh;
}

struct node* deleteF(struct node *Lh){
    struct node *t = Lh;
        

}

void display(struct node *h){
    while(h!= NULL){
        printf("%d", h->data);
        h = h -> rl;
    }
    printf("\n");
}


int main(){
    struct node *Rh=NULL, *Lh = NULL;
    Rh = insertL(2, Rh);
    Lh = Rh;
    Lh = insertF(3, Lh);
    // printf("%d %d\n",Lh ->data, Rh -> data);
    display(Lh);
}
