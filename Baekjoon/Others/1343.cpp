#include<stdio.h>

int check(char* s, int length, int start, int size) {
	if (start + size > length)
		return 0;

	for (int i = 0; i < size; i++)
	{
		if (s[start + i] != 'X')
			return 0;
	}

	return 1;
}

int main() {
	// 0 initialize
	int i, j, len;
	char s[51];
	scanf("%s", s);
	// check length of s
	for (i = 0; i < 51; i++)
	{
		if (s[i] == '\0') {
			len = i;
			break;
		}
	}
	// 1 change XXXX to AAAA
	for (i = 0; i < len; i++)
	{
		if (s[i] == 'X' && check(s, len, i, 4)) {
			for (j = 0; j < 4; j++)
			{
				s[i + j] = 'A';
			}
		}
	}
	// 2 change XX to BB
	for (i = 0; i < len; i++)
	{
		if (s[i] == 'X' && check(s, len, i, 2)) {
			for (j = 0; j < 2; j++)
			{
				s[i + j] = 'B';
			}
		}
	}
	// 3 output
	int flag = 0;
	for (i = 0; i < len; i++)
	{
		if (s[i] == 'X') {
			flag = 1;
			break;
		}
	}
	if (flag) {
		printf("-1\n");
	}
	else {
		printf("%s\n", s);
	}
	
	return 0;
}