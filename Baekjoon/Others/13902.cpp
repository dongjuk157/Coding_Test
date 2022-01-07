#include<iostream>
#include<algorithm> // fill
using namespace std;
#define INF 987654321
#define min(x, y) (x > y) ? y : x
int memo[10001];
int wok[1000];
bool amount[10001];

int main() {
	// 0 입력
	int N, M, i, j, k;
	cin >> N >> M;
	for (i = 0; i < M; i++)
		cin >> wok[i];

	// 1 하나 또는 두개의 웍을 사용해서 만들수 있는 요리의 양 계산
	for (i = 0; i < M; i++)
	{
		amount[wok[i]] = true;
		for (j = i + 1; j < M; j++) {
			if (wok[i] + wok[j] > N) continue;
			amount[wok[i] + wok[j]] = true;
		}
	}
	// 2 dp계산
	fill(memo, (memo + N + 1), INF);
	memo[0] = 0;
	for (i = 0; i <= N; i++)
		if (amount[i]) memo[i] = 1;
	for (i = 0; i <= N; i++)
	{
		for (k = 0; k <= N; k++)
		{
			if (!amount[k]) continue;
			if (i + k > N) continue;
			memo[i + k] = min(memo[i] + 1, memo[i + k]);
		}
	}
	// 3 출력
	if (memo[N] == INF)
		cout << -1 << '\n';
	else
		cout << memo[N] << '\n';
	return 0;
}
