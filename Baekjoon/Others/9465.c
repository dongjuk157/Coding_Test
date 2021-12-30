#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define max(x, y) ((x > y) ? x : y)
int s[2][100000] = { 0, };
int main() {
	int T, N, t, i, j;
	scanf("%d", &T);
	for (t = 0; t < T; t++)
	{
		int m[2][100002] = { 0, };
		scanf("%d", &N);

		for (j = 0; j < 2; j++) {
			for (i = 0; i < N; i++)
			{
				scanf("%d", &s[j][i]);
			}
		}


		for (i = 0; i < N; i++)
		{
			m[0][i] += s[0][i];
			m[1][i] += s[1][i];

			m[0][i + 1] = max(m[1][i], m[0][i + 1]);
			m[0][i + 2] = max(m[1][i], m[0][i + 2]);
			m[1][i + 1] = max(m[0][i], m[1][i + 1]);
			m[1][i + 2] = max(m[0][i], m[1][i + 2]);
		}
		printf("%d\n", max(m[0][N - 1], m[1][N - 1]));
	}
	return 0;
}