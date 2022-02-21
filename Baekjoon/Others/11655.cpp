#include<stdio.h>
#include<string.h>

int main() {
	int i, tmp;
	char s[101], *ptr;
	fgets(s, 101, stdin);
	s[strlen(s) - 1] = '\0';
	ptr = s;
	while (*ptr != '\0') {
		if ((int)'a' <= (int)(*ptr) && (int)(*ptr) <= (int)'z') {
			tmp = (((int)(*ptr) - (int)'a' + 13) % 26) + (int)'a';
			*ptr = (char)tmp;
			//printf("%c %d", tmp, tmp);
		}
		else if ((int)'A' <= (int)(*ptr) && (int)(*ptr) <= (int)'Z') {
			tmp = (((int)(*ptr) - (int)'A' + 13) % 26) + (int)'A';
			*ptr = (char)tmp;
			//printf("%c %d", tmp, tmp);
		}
		ptr++;
	}
	printf("%s", s);
	return 0;
}