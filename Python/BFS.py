from collections import deque


def BFS(start: int, graph: dict[int, list[int]], visited: list[bool]) -> None:
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        BFS(i, graph, visited)

print(visited[1:])
