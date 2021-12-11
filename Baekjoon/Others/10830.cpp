#include <iostream>
#include <vector>
using namespace std;
typedef vector<vector<long long>> matrix;
matrix operator * (const matrix a, const matrix b) {
    long long size = a.size();
    matrix ret(size, vector<long long>(size));
    long long i, j, k;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j)
        {
            for (k = 0; k < size; ++k) {
                ret[i][j] += a[i][k] * b[k][j];
            }
            ret[i][j] %= 1000;
        }
    }

    return ret;
}

matrix pow(matrix a, long long N) {
    // N: the number of multiply (num_m times)
    long long size = a.size();
    matrix ret(size, vector<long long>(size));
    if (N == 1) {
        matrix unit(size, vector<long long>(size));
        for (long long i = 0; i < size; i++)
        {
            unit[i][i] = 1;
        }
        ret = a * unit;
        return ret;
    }

    matrix tmp(size, vector<long long>(size));
    tmp = pow(a, N / 2);
    if (N % 2) { // odd
        ret = tmp * tmp * a;
    }
    else { //even
        ret = tmp * tmp;
    }
    return ret;
}

int main() {
    // 0. 입력
    // 0-1. 변수 입력
    long long N, B, i, j;
    cin >> N >> B;
    // 0-2. 동적할당을 사용해서 n by n matrix 생성
    matrix mat(N, vector<long long>(N));
    matrix ret(N, vector<long long>(N));
    for (i = 0; i < N; ++i) {
        for (j = 0; j < N; ++j) {
            cin >> mat[i][j];
        }
    }
    // 1. 분할정복
    ret = pow(mat, B);
    for (i = 0; i < N; ++i) {
        for (j = 0; j < N; ++j) {
            cout << ret[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}