#include<iostream>
#include<string> // for to_string, stoi
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int S = 0;
    int M, num;
    string c;
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> c;
        switch (c[1])
        {
        case 'd': // add
            cin >> num;
            S |= (1 << (num - 1));
            break;
        case 'e': // remove
            cin >> num;
            S &= ~(1 << (num - 1));
            break;
        case 'h': // check
            cin >> num;
            if ((S >> (num - 1)) & 1)
                cout << "1\n";
            else
                cout << "0\n";
            break;
        case 'o': // toggle
            cin >> num;
            S = ((S >> (num - 1)) & 1) ? S & ~(1 << (num - 1)) : S | (1 << (num - 1));
            break;
        case 'l': // all
            S = (1 << 21) - 1;
            break;
        case 'm': // empty
            S = 0;
            break;
        default:
            break;
        }

    }
    return 0;
}
