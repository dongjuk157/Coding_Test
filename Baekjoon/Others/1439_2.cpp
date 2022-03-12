#include<stdio.h>

int main() {
	int cnt=0;
	char p='\0', c;
	while (1)
	{
		c = getchar();
		if (c == '\0' || c == '\n') {
			break;
		}
		if (p != c)
			cnt++;
		p = c;
	}
	printf("%d\n", cnt / 2);
	return 0;
}
