def DFS_For_TopSort(u: int, graph: dict[int, list[int]], visited: list[bool], res: list[int]):
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            DFS_For_TopSort(v, graph, visited, res)

    res.append(u)


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
sorted_vertexes = []

for i in range(1, n + 1):
    if not visited[i]:
        DFS_For_TopSort(i, graph, visited, sorted_vertexes)

print(*sorted_vertexes[::-1])


# ВАЖНО ПРОВЕРИТЬ, ЧТО В ГРАФЕ НЕТ ЦИКЛОВ
