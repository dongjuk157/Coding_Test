#include<iostream>
#include<vector>
using namespace std;
typedef long long ll;
typedef vector<vector<ll>> matrix;

#define DIVMOD 1000000007;

matrix operator *(matrix a, matrix b) {
	ll i, j, k;
	matrix ret(2, vector<ll>(2));
	for (i = 0; i < a.size(); ++i)
	{
		for (j = 0; j < a.size(); ++j)
		{
			for (k = 0; k < a.size(); ++k)
			{
				ret[i][j] += (a[i][k] * b[k][j]);
			}
			ret[i][j] %= DIVMOD;
		}
	}
	return ret;
}

matrix findFibo(ll num) {
	matrix base_matrix(2, vector<ll>(2, 1));
	base_matrix[1][1] = 0;
	
	if (num < 2) {
		return base_matrix;
	}

	matrix ret(2, vector<ll>(2));
	ret = findFibo(num / 2);
	if (num % 2) {
		return ret * ret * base_matrix;
	} else {
		return ret * ret;
	}
}
int main() {
	ll n;
	cin >> n;
	matrix ans = findFibo(n-1);
	cout << ans[0][0] << endl;
	return 0;
}