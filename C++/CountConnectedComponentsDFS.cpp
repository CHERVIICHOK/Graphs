#include <iostream>
#include <vector>

using std::vector;

void dfs(int u, const vector<vector<int>>& graph, vector<bool>& visited) {
    visited[u] = true;

    for (int v : graph[u]) {
        if (!visited[v]) {
            dfs(v, graph, visited);
        }
    }
}

int main () {
    using std::cin;
    using std::cout;

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);

    }

    vector<bool> visited(n + 1, false);

    int count = 0;
    for (int i = 1; i < n + 1; i++) {
        if (!visited[i]) {
            count++;
            dfs(i, graph, visited);
        }
    }

    cout << count;
}
