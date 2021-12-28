#include<iostream>
#include<vector>
#include<queue>
#include<array>
using namespace std;

int bfs(array<int, 3> start, array<int, 3> end, array<int, 3> size, vector<vector<string>>building) {
	queue<array<int, 3>> q;
	q.push(start);
	q.empty();
	vector<vector<vector<int>>> visit(size[0]+2, vector<vector<int>>(size[1]+2, vector<int>(size[2]+2)));
	visit[start[0]][start[1]][start[2]] = 1;
	int d[6][3] = {{ 1, 0, 0 },{ -1, 0, 0 },{ 0, 1, 0 },{0, -1, 0 },{ 0, 0, 1 },{ 0, 0, -1 }};
	while (!q.empty()) {
		array <int, 3> cur;
		cur = q.front();
		q.pop();
		
		for (int i = 0; i < 6; i++)
		{
			int dl, dr, dc;
			dl = cur[0] + d[i][0];
			dr = cur[1] + d[i][1];
			dc = cur[2] + d[i][2];

			if (building[dl][dr][dc] == '#') continue;
			if (visit[dl][dr][dc]) continue;
			visit[dl][dr][dc] = visit[cur[0]][cur[1]][cur[2]] + 1;
			array <int, 3> tmp = { dl, dr, dc };
			q.push(tmp);

		}
	}
	if (visit[end[0]][end[1]][end[2]]) {
		return visit[end[0]][end[1]][end[2]] - 1;
	}
	return 0;
}

int main() {
	while (1) {
		int L, R, C, answer;
		string remove;
		array<int, 3> start, end, size;
		vector<vector<string>> building;

		cin >> L >> R >> C;
		if (L == 0 && R == 0 && C == 0)			break;
		size = { L, R, C };
		for (int i = 0; i < L+2; i++)
		{
			vector<string> tmp_l;
			for (int j = 0; j < R + 2; j++)
			{
				string tmp_r;
				if (0 == j || R + 1 == j || 0 == i || L + 1 == i) {
					for (int k = 0; k < C + 2; k++)
					{
						tmp_r += "#";
					}
				}
				else {
					string tmp_string;
					cin >> tmp_string;
					tmp_r = "#" + tmp_string + "#";
					for (int k = 0; k < C + 2; k++)
					{
						if ('S' == tmp_r[k]) {
							start = { i,j,k };
						}
						else if ('E' == tmp_r[k]) {
							end = { i,j,k };
						}
					}
				}
				tmp_l.push_back(tmp_r);
			}
			building.push_back(tmp_l);
		}
		answer = bfs(start, end, size, building);

		if (answer) {
			cout << "Escaped in " << answer << " minute(s)." << endl;
		}
		else {
			cout << "Trapped!" << endl;
		}
	}
	return 0;
}

