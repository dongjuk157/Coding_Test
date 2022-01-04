#include<iostream>
#include<queue>
#include<vector>
using namespace std;

#define p pair<int, int>
#define pp pair<int, p>

string map[50];

int dijkstra(int N) {
	int cost, r, c, i, dr, dc;
	vector<vector<bool>> visit(N, vector<bool>(N, false));

	priority_queue<pp> h;
	int d[8] = { 0, 1, 1, 0, -1, 0, 0, -1 };
	h.push(pp(0, p(0, 0)));
	while (!h.empty()) {
		pp cur = h.top(); h.pop();
		cost = -cur.first;
		r = cur.second.first;
		c = cur.second.second;
		if (r == N - 1 && c == N - 1)
			return cost;
		if (visit[r][c])
			continue;
		visit[r][c] = true;
		for (i = 0; i < 4; i++)
		{
			dr = r + d[2 * i];
			dc = c + d[2 * i + 1];
			if (dr < 0 || dr >= N || dc < 0 || dc >= N)
				continue;

			if (map[dr][dc] == '1') {
				h.push(pp(-cost, p(dr, dc)));
			}
			else {
				h.push(pp(-(cost + 1), p(dr, dc)));
			}
		}
	}
	return -1;
}

int main() {
	int N, i;
	cin >> N;
	for (i = 0; i < N; i++)
		cin >> map[i];
	cout << dijkstra(N);
	return 0;
}