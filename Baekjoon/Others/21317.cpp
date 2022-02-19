#include<iostream>
#include<vector>
using namespace std;

int find_energy(int n, int super_jump, int jump[20][2]) {
	int i, j, cur, cur_chance, ret;
	vector<pair<int, int>> memo[20];
	memo[0].push_back(make_pair(0, 1));
	for (i = 0; i < n; i++)
	{
		//cout << memo[i].size() << endl;
		for (j = 0; j < memo[i].size(); j++)
		{
			cur = memo[i][j].first;
			cur_chance = memo[i][j].second;
			if (i + 1 < n)
			{
				memo[i + 1].push_back(make_pair(cur + jump[i][0], cur_chance));
			}
			if (i + 2 < n) {
				memo[i + 2].push_back(make_pair(cur + jump[i][1], cur_chance));
			}
			if (cur_chance && i + 3 < n) {
				memo[i + 3].push_back(make_pair(cur + super_jump, 0));
			}
		}
	}
	ret = 200000;
	for (i = 0; i < memo[n - 1].size(); i++)
	{
		if (ret > memo[n - 1][i].first)
			ret = memo[n - 1][i].first;
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int n, i, j, k;
	int jump[20][2];
	cin >> n;
	for (i = 0; i < n - 1; i++)
	{
		cin >> jump[i][0] >> jump[i][1];
	}
	cin >> k;

	cout << find_energy(n, k, jump);

	return 0;
}