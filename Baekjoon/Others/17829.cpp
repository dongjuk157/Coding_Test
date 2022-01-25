#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int arr[1024][1024] = { 0 };

int find_second_max(int r, int c, int size) {
    int tmp[4] = { arr[r][c], arr[r + size][c], arr[r][c + size], arr[r + size][c + size] };
    sort(tmp, tmp + 4);
    return tmp[2];
}
int main() {
    // 0 init
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, i, j, size, tmp_i, tmp_j;
    // 1 input
    cin >> N;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            cin >> arr[i][j];

    // 2 222 pulling
    size = N;
    while (size != 1) {
        for (i = 0; i < size / 2; i++) {
            for (j = 0; j < size / 2; j++) {
                tmp_i = N / size * i * 2;
                tmp_j = N / size * j * 2;
                arr[tmp_i][tmp_j] = find_second_max(tmp_i, tmp_j, N / size);
            }
        }
        size >>= 1;
    }
    // 3 output
    cout << arr[0][0] << '\n';

    return 0;
}