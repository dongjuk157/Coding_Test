#include<iostream>
#include<queue>
#include<string>
using namespace std;
#define D(s) ((2 * (s)) % 10000)
#define S(s) (((s) + 9999) % 10000)
#define L(s) (((s) % 1000) * 10 + ((s) / 1000))
#define R(s) (((s) / 10) + (((s) % 10) * 1000))

string bfs(int s, int e) {
	int cur, next, tmp;
	bool visit[10000] = { 0, };
	string cur_c, next_c;
	queue<pair<int, string>> q;
	q.push(make_pair(s, ""));
	while (!q.empty())
	{
		cur = q.front().first;
		cur_c = q.front().second;
		q.pop();
		if (cur == e)
			return cur_c;

		tmp = D(cur);
		if (!visit[tmp]) {
			visit[tmp] = true;
			q.push(make_pair(tmp, cur_c + "D"));
		}
		tmp = S(cur);
		if (!visit[tmp]){
			visit[tmp] = true;
			q.push(make_pair(tmp, cur_c + "S"));
		}
		tmp = L(cur);
		if (!visit[tmp]) {
			visit[tmp] = true;
			q.push(make_pair(tmp, cur_c + "L"));
		}
		tmp = R(cur);
		if (!visit[tmp]) {
			visit[tmp] = true;
			q.push(make_pair(tmp, cur_c + "R"));
		}
	}
	return "";
}

int main() {
	int t, i, s, e;
	string answer;
	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> s >> e;
		cout << bfs(s, e) << '\n';
	}
	return 0;
}