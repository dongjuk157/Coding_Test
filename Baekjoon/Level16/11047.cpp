#include<iostream>

using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, K, i, s, answer = 0;
    int v[10];
    cin >> N >> K;
    for (i = 0; i < N; i++){
        cin >> v[i];
    }
    i = N - 1;
    while ((0 != K) || (-1 != i)) {
        if (v[i] > K) continue;
        s = K / v[i];
        K -= s * v[i];
        answer += s;
    }
    cout << answer << '\n';
    return 0;
}