#include<iostream>
using namespace std;

bool owned[(1 << 20) + 1] = { 0, };
int check_owned(int x) {
    int land = 0;
    while (x)
    {
        if (owned[x])
            land = x;
        x >>= 1;
    }
    return land;
}

int main() {
    int N, Q, i, num, land;
    cin >> N >> Q;

    for (i = 0; i < Q; i++)
    {
        cin >> num;
        land = check_owned(num);
        if (!land)
            owned[num] = true;
        cout << land << '\n';

    }

    return 0;
}
