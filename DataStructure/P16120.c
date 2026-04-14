# include <stdio.h>
# include <stdlib.h>
# include <string.h>

typedef struct Node {
    char c;
    struct Node* next;
} Node;

Node* createNode(char c) {
    Node* newNode = (Node *)malloc(sizeof(Node));
    newNode->c = c;
    newNode->next = NULL;
    return newNode;
}

void push(Node** top, char c) {
    Node* newNode = createNode(c);
    newNode->next = *top;
    *top = newNode;
}

void pop(Node** top) {
    if (*top == NULL) return;

    Node* temp = *top;
    *top = temp->next;
    free(temp);
}

int main() {
    char input[1000001];
    scanf("%s", input);

    Node* stack = NULL;
    int size = 0;

    for (int i = 0; input[i] != '\0'; i++) {
        push(&stack, input[i]);
        size++;

        Node* t1 = stack;
        if (size >= 4 && stack->c == 'P') {
            Node* t2 = t1->next;
            Node* t3 = t2->next;
            Node* t4 = t3->next;

            if (t2->c == 'A' && t3->c =='P' && t4->c == 'P') {
                for (int j = 0; j < 3; j++) pop(&stack);
                size -= 3;
            }
        }
    }

    if (stack->c == 'P' && size == 1) printf("PPAP\n");
    else (printf("NP\n"));
}