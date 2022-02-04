#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int main() {
	//ios::sync_with_stdio(false);
	//cin.tie(NULL); cout.tie(NULL);
	char s[501], tmpc;
	int tmp = 0, null_ind, i;
	while (1) {
		scanf(" %[^\n]s", s);
		if (s[0] == 'E' && s[1] == 'N' && s[2] == 'D' && s[3] == '\0') break;

		// find s.end()
		null_ind = 0;
		for (i = 0; i < 501; i++)
		{
			if (s[i] == '\0'){
				null_ind = i;
				break;
			}
		}
		//reverse(s.begin(), s.end());
		for (i = 0; i < null_ind / 2; i++)
		{
			tmpc = s[i];
			s[i] = s[null_ind - 1 - i];
			s[null_ind - 1 - i] = tmpc;
		}

		// cout << s << '\n';
		printf("%s\n", s);

	}

	return 0;
}