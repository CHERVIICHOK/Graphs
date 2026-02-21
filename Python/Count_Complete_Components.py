def DFS(u: int, graph: dict[int, list[int]], visited: list[bool]) -> None:
    visited[u] = True

    for adj_vertex in graph[u]:
        if not visited[adj_vertex]:
            DFS(adj_vertex, graph, visited)


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i, graph, visited)

print(count)
