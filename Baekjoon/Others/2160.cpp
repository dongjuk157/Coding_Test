#include <cstdio>

// functions
void array_input(int);
int find_combination(int);
void find_answer(int);
int check_diff(int, int);

// global variables
char pictures[50][5][7];
int combination[50*49];
int answer[2];

// implement
int main() {
	int N, size;

	// int answer[2] global
	scanf(" %d", &N);
	array_input(N);
	size = find_combination(N);
	find_answer(size / 2);

	printf("%d %d\n", answer[0], answer[1]);

	return 0;
}

void array_input(int array_size) {
	int i, j, k;
	char tmp[10];
	for (i = 0; i < array_size; i++) {
		for (j = 0; j < 5; j++) {
			scanf("%s", tmp);
			for (k = 0; k < 7; k++){
				pictures[i][j][k] = tmp[k];
			}
		}
	}
}

int find_combination(int size) {
	int i, j, tmp;
	tmp = 0;
	for (i = 0; i < size; i++)
	{
		for (j = i + 1; j < size; j++)
		{
			combination[tmp] = i;
			combination[tmp + 1] = j;
			tmp += 2;
		}
	}

	return tmp;
}

int check_diff(int pic1, int pic2) {
	int ret = 0;
	int r, c;
	for (r = 0; r < 5; r++)
		for (c = 0; c < 7; c++)
			if (pictures[pic1][r][c] != pictures[pic2][r][c])
				ret++;
	return ret;
}

void find_answer(int size) {
	int i, tmp, diff = 36;
	for (i = 0; i < size; i++)
	{
		tmp = check_diff(combination[2 * i], combination[2 * i + 1]);
		if (diff > tmp)
		{
			diff = tmp;
			answer[0] = combination[2 * i] + 1;
			answer[1] = combination[2 * i + 1] + 1;
		}
	}
}

