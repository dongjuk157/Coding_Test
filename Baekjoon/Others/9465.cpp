#include<iostream>
#include<vector>
using namespace std;

#define max(x, y) ((x > y) ? x : y)

int main() {
	int T, N, tc, i, j, num_tmp;
	cin >> T;
	for (tc = 0; tc < T; tc++)
	{
		cin >> N;
		vector<vector<int>> sticker;
		vector<vector<int>> memo(2, vector<int>(N, 0));

		for (j = 0; j < 2; j++) {
			vector<int> tmp;
			for (i = 0; i < N; i++)
			{
				num_tmp;
				cin >> num_tmp;
				tmp.push_back(num_tmp);
			}
			sticker.push_back(tmp);
		}

		for (i = 0; i < N; i++)
		{
			memo[0][i] = sticker[0][i];
			memo[1][i] = sticker[1][i];
			if (i == 0) {}
			else if (i == 1) {
				memo[0][i] += memo[1][i - 1];
				memo[1][i] += memo[0][i - 1];
			}
			else {
				memo[0][i] += max(memo[1][i - 1], memo[1][i - 2]);
				memo[1][i] += max(memo[0][i - 1], memo[0][i - 2]);
			}
		}
		cout << max(memo[0][N - 1], memo[1][N - 1]) << endl;
	}
	return 0;
}