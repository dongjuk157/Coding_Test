#include<cstdio>
#include<cstring>

int check_anagram(char* str1, char* str2) {
	int i, str1_arr[26] = { 0, }, str2_arr[26] = { 0, };
	if (strlen(str1) != strlen(str2)) {
		return 0;
	}
	for (i = 0; i < strlen(str1); i++)
	{
		str1_arr[(int)str1[i] - (int)'a']++;
		str2_arr[(int)str2[i] - (int)'a']++;
	}
	for (i = 0; i < 26; i++)
	{
		if (str1_arr[i] != str2_arr[i]) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int t, i, chk;
	char tmp1[102], tmp2[102];
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%s %s", tmp1, tmp2);
		chk = check_anagram(tmp1, tmp2);
		printf("%s & %s are ", tmp1, tmp2);
		if (!chk) {
			printf("NOT ");
		}
		printf("anagrams.\n");
	}

	return 0;
}