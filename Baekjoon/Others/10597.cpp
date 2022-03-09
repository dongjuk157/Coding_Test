#include<stdio.h>
#include<stdlib.h> // exit

int visit[51] = { 0, };
int stack[51] = { 0, };
int stack_idx = 0;
char s[100];
int change_int(int size, char first, char second) {
    int ret;
    ret = first - '0';
    if (size == 1)
        return ret;
    ret *= 10;
    ret += second - '0';
    return ret;
}

void backtrack(int ind, int limit) {
    if (ind == limit) {
        int max = 0;
        int i;
        for (i = 1; i < 51; i++)
        {
            if (visit[i]) {
                max = i;
            }
        }
        for (i = 1; i < max + 1; i++)
        {
            if (!visit[i]) {
                return;
            }
        }

        // print length and all stack
        for (i = 0; i < stack_idx; i++)
        {
            printf("%d ", stack[i]);
        }
        printf("\n");
        exit(0);
    }
    int tmp;
    tmp = change_int(1, s[ind], 0);
    
    if (tmp && !visit[tmp]) {
        visit[tmp] = 1;
        stack[stack_idx++] = tmp;
        backtrack(ind + 1, limit);
        visit[tmp] = 0;
        stack_idx--;
    }
    if (ind + 2 <= limit) {
        tmp = change_int(2, s[ind], s[ind + 1]);
        if (tmp <= 50 && !visit[tmp]) {
            visit[tmp] = 1;
            stack[stack_idx++] = tmp;
            backtrack(ind + 2, limit);
            visit[tmp] = 0;
            stack_idx--;
        }
    }
}

int main() {
    int len, i;
    scanf("%s", s);
    for (i = 0; i < 100; i++)
    {
        if (s[i] == '\0') {
            len = i;
            break;
        }
    }
    backtrack(0, len);

    return 0;
}