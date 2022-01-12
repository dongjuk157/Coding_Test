#include<iostream>
#include<vector>
#define max(x, y) (x < y) ? y : x
using namespace std;

int answer, H;
vector<pair<int, int>> mint_choco;
vector<bool> visit;
pair<int, int> start;

int abs(int x) {
	return (x < 0) ? -x : x;
}

int dist(pair<int, int> a, pair<int, int> b) {
	return abs(a.first - b.first) + abs(a.second - b.second);
}

void dfs(int ind, int M, pair<int,int> last, int total) {
	if (ind) {
		if (dist(last, start) <= M) {
			answer = max(answer, total);
		}
	}
	if (ind == mint_choco.size()) return;

	for (int i = 0; i < mint_choco.size(); i++)
	{
		if (visit[i]) continue;
		if (M < dist(last, mint_choco[i])) continue;
		visit[i] = true;
		dfs(ind + 1, M + H - dist(last, mint_choco[i]), mint_choco[i], total + 1);
		visit[i] = false;
	}
}

int main() {
	//ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N, M, i, j, tmp;
	cin >> N >> M >> H;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
		{
			cin >> tmp;
			if (tmp == 1) {
				start.first = i;
				start.second = j;
			}
			else if (tmp == 2) {
				mint_choco.push_back(make_pair(i, j));
			}
		}
	}
	for (i = 0; i < mint_choco.size(); i++)
	{
		visit.push_back(0);
	}
	dfs(0, M, start, 0);
	cout << answer << '\n';
	return 0;
}