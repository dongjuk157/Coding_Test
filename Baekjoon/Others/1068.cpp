#include<iostream>
#include<vector>
using namespace std;

int answer = 0;

void preorder(int cur_node, int removed_node, vector<vector<int>> node_son) {
	if (cur_node == removed_node) return ;
	if ((node_son[cur_node].empty())
		|| ((1 == node_son[cur_node].size()) && removed_node == node_son[cur_node][0])
	) {
		answer += 1;
		return;
	}
	for (int i = 0; i < node_son[cur_node].size(); i++)
	{
		int son = node_son[cur_node][i];
		preorder(son, removed_node, node_son);
	}
}

int main() {
	// 0 입력
	int N, root, removed_node;
	cin >> N;
	vector<int> node_parent(N);
	vector<vector<int>> node_son(N);

	for (int i = 0; i < N; i++)
	{
		cin >> node_parent[i];
		if (node_parent[i] == -1) {
			root = i;
			continue;
		}
		// add son
		node_son[node_parent[i]].push_back(i);
	}
	cin >> removed_node;

	// 1 탐색
	preorder(root, removed_node, node_son);

	// 2 출력
	cout << answer;

	return 0;
}