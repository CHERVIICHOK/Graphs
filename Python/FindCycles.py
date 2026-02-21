def DFS_For_Find_Cycles(u: int, graph: dict[int, list[int]], visited: list[int], stack: list[int]) -> None:
    visited[u] = 1
    stack.append(u)

    for v in graph[u]:
        if visited[v] == 0:
            DFS_For_Find_Cycles(v, graph, visited, stack)
        elif visited[v] == 1:
            print('Cycle!')
            print(f'Path: {stack[stack.index(v):]}\n')

    stack.pop()
    visited[u] = 2


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [0] * (n + 1)
stack = []

for i in range(1, n + 1):
    if visited[i] == 0:
        DFS_For_Find_Cycles(i, graph, visited, stack)
