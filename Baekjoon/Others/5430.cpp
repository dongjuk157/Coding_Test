#include<iostream>
#include<string> // stoi, to_string
using namespace std;

int arr[100000];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T, N, idx, i, start_idx, end_idx;
	bool forward, error;
	string p, tmp, tmp_num, answer;
	cin >> T;
	while (T) {
		T--;
		cin >> p >> N >> tmp;

		idx = 0;
		tmp_num = "";
		for (i = 1; i < tmp.length(); i++)
		{
			if (tmp[i] == ',' || tmp[i] == ']') {
				if (tmp_num == "") {
					continue;
				}
				arr[idx] = stoi(tmp_num);
				idx++;
				tmp_num = "";
				continue;
			}
			tmp_num += tmp[i];
		}

		start_idx = 0;
		end_idx = N;
		forward = true; // array traversal direction
		error = false;

		for (i = 0; i < p.length(); i++)
		{
			if (p[i] == 'R') {
				forward = !forward;
			}
			else if (p[i] == 'D')
			{
				if (start_idx == end_idx) {
					error = true;
					break;
				}
				else {
					if (forward) {
						start_idx++;
					}
					else {
						end_idx--;
					}

				}
			}
		}
		answer = "";
		if (error) {
			cout << "error\n";
		}
		else {
			answer = "[";
			if (forward)
			{
				for (i = start_idx; i < end_idx; i++)
				{
					answer += to_string(arr[i]);
					if (i < end_idx - 1)
						answer += ',';
				}
			}
			else {
				for (i = end_idx - 1; i >= start_idx; i--)
				{
					answer += to_string(arr[i]);
					if (i > start_idx)
						answer += ',';
				}
			}
			answer += "]\n";
		}
		cout << answer;
	}
	return 0;
}