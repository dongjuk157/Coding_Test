#include<iostream>
#include<vector>
using namespace std;

#define max(x,y) (x > y) ? x : y

int main() {
	string a, b;
	cin >> a >> b;
	vector<vector<int>> t(b.length() + 1, vector<int>(a.length() + 1, 0));
	for (int i = 0; i < b.length(); i++)
	{
		for (int j = 0; j < a.length(); j++) {
			t[i + 1][j + 1] = max(t[i + 1][j], t[i][j + 1]);
			if (a[j] == b[i])
				t[i + 1][j + 1] = max(t[i + 1][j + 1], t[i][j] + 1);
		}
	}
	cout << t[b.length()][a.length()] << '\n';

	return 0;
}