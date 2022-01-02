#include<iostream>
#include<cstring>
using namespace std;
#define INF 987654321
int N;
int d[20][20];
int m[29][1 << 20];

int bt(int ind, int limit, int state) {
	if (ind == limit) return 0;
	if (m[ind][state] != -1) return m[ind][state];

	m[ind][state] = INF;
	for (int i = 0; i < limit; i++)
	{
		if (state & (1 << i)) continue;
		int next_state = state | (1 << i);
		int next_val = bt(ind + 1, limit, next_state) + d[ind][i];
		if (next_val < m[ind][state]) {
			m[ind][state] = next_val;
		}
	}
	return m[ind][state];
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> d[i][j];
	memset(m, -1, sizeof(m));
	cout << bt(0, N, 0);

	return 0;
}