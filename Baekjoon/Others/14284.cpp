#include<iostream>
#include<vector>
#include<queue>
using namespace std;
#define INF 1234567890

int dijkstra(int start, int end, int size, vector<vector<pair<int, int>>> linked_list) {
	int cur, cur_dist, adj, adj_dist, i;
	priority_queue<pair<int, int>> min_h;
	vector<int> visit(size + 1, INF);
	min_h.push(make_pair(0, start));
	while (!min_h.empty())
	{
		cur_dist = -min_h.top().first;
		cur = min_h.top().second;
		min_h.pop();
		if (cur == end)
			return cur_dist;
		visit[cur] = cur_dist;
		for (i = 0; i < linked_list[cur].size(); i++)
		{
			adj_dist = linked_list[cur][i].first;
			adj = linked_list[cur][i].second;
			if (visit[adj] > adj_dist + cur_dist) {
				min_h.push(make_pair(-(adj_dist + cur_dist), adj));
			}
		}
	}
	return INF;
}


int main()
{
	//ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n, m, a, b, c, s, t, i, j;
	cin >> n >> m;
	vector<vector<pair<int, int>>> linked_list(n + 1);
	for (i = 0; i < m; i++)
	{
		cin >> a >> b >> c;
		linked_list[a].push_back(make_pair(c, b));
		linked_list[b].push_back(make_pair(c, a));
	}
	cin >> s >> t;

	cout << dijkstra(s, t, n, linked_list) << '\n';

	return 0;
}