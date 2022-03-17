#include<iostream>
#include<string>
#include<set>

using namespace std;

struct Compare {
    bool operator() (const string& a, const string& b) const {
        return stoll(a, 0, 16) > stoll(b, 0, 16);
    };
};

long long find_number(string s, int real_length, int split_length, int order) {
    long long ret = 0;
    set<string, Compare> ans;
    for (int i = 0; i < split_length; i++)
    {
        for (int j = i; j < i + real_length; j += split_length)
        {
            ans.insert(s.substr(j, split_length));
        }
    }
    int cnt = 0;
    for (auto str16: ans)
    {
        cnt++;
        if (cnt == order) {
            ret = stoll(str16, 0, 16);
            cout << ret<< endl;
        }
    }
    return ret;
}

int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        int n, k;
        string s;
        cin >> n >> k >> s;
        s += s.substr(0, n / 4);
        cout << "#" << test_case << " " << find_number(s, n, n / 4, k) << endl;
    }
    return 0;
}