# include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int pos[1001];
    // 배열 초기화
    for (int i = 0; i < 1001; i++) {
        pos[i] = 0;
    }

    for (int i = 0; i < N; i++) {
        int L, H;
        scanf("%d %d", &L, &H);
        pos[L] = H;
    }

    int max_height = 0;
    int max_height_pos = 0;
    for (int i = 0; i <= 1000; i++) {
        if (max_height < pos[i]) {
            max_height = pos[i];
            max_height_pos = i;
        }
    }

    int answer = 0;
    int cur_height = 0;
    for (int i = 0; i < max_height_pos; i++) {
        if (cur_height < pos[i]) {
            cur_height = pos[i];
        }
        answer += cur_height;
    }

    cur_height = 0;
    for (int i = 1000; i > max_height_pos; i--) {
        if (cur_height < pos[i]) {
            cur_height = pos[i];
        }
        answer += cur_height;
    }

    answer += max_height;
    printf("%d\n", answer);
}