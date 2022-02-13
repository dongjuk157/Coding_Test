#include<iostream>
#include<algorithm>
#define INF 987654321
using namespace std;

void init();
void floyd();
void output();

int n, m;
int cost[100][100] = { 0, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	init();
	floyd();
	output();

	return 0;
}
void init() {
	int i, j, a, b, c;
	cin >> n >> m;
	// initialize array
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (i != j)
				cost[i][j] = INF;
		}
	}

	// input cost
	for (i = 0; i < m; i++)
	{
		cin >> a >> b >> c;
		if (cost[a - 1][b - 1])
			cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c);
		else
			cost[a - 1][b - 1] = c;
	}
}
void floyd() {
	int i, j, k, tmp;
	for (k = 0; k < n; k++)
	{
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
			}
		}
	}

}
void output() {
	int i, j;
	// post processing and print
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (cost[i][j] == INF)
				cost[i][j] = 0;
			cout << cost[i][j] << ' ';
		}
		cout << '\n';
	}
}