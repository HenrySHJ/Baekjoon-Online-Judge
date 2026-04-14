# include <stdio.h>
# include <stdlib.h>
# include <string.h>

typedef struct station {
    int number;
    struct station* prev;
    struct station* next;
} station;

station* addr[1000001];

station* createStation(int number) {
    station* s = (station *)malloc(sizeof(station));
    s->number = number;
    s->prev = NULL;
    s->next = NULL;
    addr[number] = s;
    return s;
}

// cursor 다음 위치에 open 설립
void BN(int i, int j) {
    station* cur = addr[i];
    station* target = cur->next;

    printf("%d\n", target->number);

    station* ns = createStation(j);

    ns->next = target;
    ns->prev = cur;
    cur->next = ns;
    target->prev = ns;
}

void BP(int i, int j) {
    station* cur = addr[i];
    station* target = cur->prev;

    printf("%d\n", target->number);

    station* ns = createStation(j);

    ns->next = cur;
    ns->prev = target;
    cur->prev = ns;
    target->next = ns;
}

void CN(int i) {
    station* cur = addr[i];
    station* target = cur->next;

    printf("%d\n", target->number);

    target->prev->next = target->next;
    target->next->prev = target->prev;
    addr[target->number] = NULL;
    free(target);
}

void CP(int i) {
    station* cur = addr[i];
    station* target = cur->prev;

    printf("%d\n", target->number);

    target->prev->next = target->next;
    target->next->prev = target->prev;
    addr[target->number] = NULL;
    free(target);
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    // Cursor로 현재 위치 표현
    station* first = NULL;
    station* last = NULL;

    int num;
    for (int i = 0; i < N; i++) {
        scanf("%d", &num);

        station* ns = createStation(num);

        // 첫 노드
        if (first == NULL) {
            first = ns;
            last = ns;
        }
        // 마지막 노드 이중 연결
        else {
            last->next = ns;
            ns->prev = last;
            last = ns;
        }
    }

    // 원형 연결
    last->next = first;
    first->prev = last;

    char cmd[3];
    int i, j;

    for (int m = 0; m < M; m++) {
        scanf("%s", cmd);

        if (cmd[0] == 'B') {
            scanf("%d %d", &i, &j);
            if (cmd[1] == 'N') {
                BN(i, j);
            }
            else {
                BP(i, j);
            }
        } 
        else if (cmd[0] == 'C') {
            scanf("%d", &i);
            if (cmd[1] == 'N') {
                CN(i);
            }
            else {
                CP(i);
            }
        }
    }
    return 0;
}