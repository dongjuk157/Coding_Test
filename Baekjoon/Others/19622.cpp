#include<iostream>
using namespace std;
#define max(x, y) (x > y) ? x : y

int main(){
	cin.tie(0);
	ios::sync_with_stdio(0);
    int N, i, s, e, m;
    int memo[100000];
    cin >> N;
    for (i = 0; i < N; i++){
        cin >> s >> e >> m;
        if (i == 0)         memo[i] = m;
        else if (i == 1)    memo[i] = max(memo[i-1], m);
        else                memo[i] = max(memo[i-1], memo[i-2]+m);
    }
    cout << memo[N-1] << '\n';
    return 0;
}