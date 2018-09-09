#include <stdio.h>
#include <stdlib.h>


struct node {
    int data;
    struct node *next;
};

struct node* head;


void insert(int data){
    struct node *t = head;
    if ( head == NULL ){
        head = (struct node*)(malloc(sizeof(struct node)));
        head->data = data;
        head->next = NULL;
        return;
    }

    while ( t -> next != NULL){
        t = t->next;
    }


    t->next = (struct node*)(malloc(sizeof(struct node)));
    t->next->next = NULL;
    t->next->data = data;
}

void debug(){
    struct node *t = head;
    while(t!=NULL){
        printf("%d ", t->data);;;
        t = t->next;
    }
    printf("\n");

}

void reverse(){ 
    struct node* prev    = NULL;	//initialized 3 ptrs prev , current , next with the given values.
    struct node* current = head;	
    struct node* next;
     
     while (current != NULL)	//terminating condition , the last node's next ptr would be NULL.
    {
        next  = current->next;	//next ptr stores the original ptr (of the current node) pointing to the next node.	
        current->next = prev;	//now the direction of the above original ptr is flipped by taking the value of the prev ptr.
       
	 prev = current;	//next 2 steps are update steps, prev ptr now points to current node.
        current = next;		//current ptr now points to the next node.
    }
     head = prev;		//after termination of the while loop the head will to the node which the prev pointer is pointing , i.e the last node.
     		
    
}


int main(int argc, char *argv[]){
    head = NULL;
    int i;
    for(i=1; i<=10; i++){
        insert(i);
    }
    debug();
    reverse();
    debug();
    return 0;
}