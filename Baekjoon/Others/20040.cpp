#include<iostream>
using namespace std;
int p[500000];

int find(int a) {
	if (p[a] == a)
		return a;
	return p[a] = find(p[a]);
}

int cycle_check_or_union(int a, int b) {
	a = find(a);	b = find(b);
	// cycle_check
	if (a == b)
		return 1;
	// union
	p[b] = a;
	return 0;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);cout.tie(NULL);

	int N, M, i, j, u, v;
	cin >> N >> M;
	for (i = 0; i < N; i++) {
		p[i] = i;
	}
	for (i = 0; i < M; i++) {
		cin >> u >> v;
		if (cycle_check_or_union(u, v)) {
			cout << i + 1 << '\n';
			return 0;
		}
	}
	cout << "0\n";

	return 0;
}