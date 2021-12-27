#include<iostream>
#include<algorithm>
using namespace std;

bool isPal(string a) {
	for (int i = 0; i < a.length() / 2; i++)
	{
		if (a[i] != a[a.length() - i - 1]) {
			return false;
		}
	}
	return true;
}
int main() {
	string real_string;
	cin >> real_string;
	int answer = 0;

	string a, b;
	a = real_string;
	b = real_string;
	reverse(b.begin(), b.end());
	for (int i = 0; i < real_string.length(); i++)
	{
		string tmp;
		tmp = a + b.substr(b.length() - i, i);
		if (isPal(tmp)) {
			answer = tmp.length();
			break;
		}
	}
	cout << answer << endl;
	return 0;
}