import sys

input = sys.stdin.readline


cnt = 0


def dfs(graph, v, visited):
    visited[v] = True
    global cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1


N = int(input())
line = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(graph, 1, visited)
print(cnt)


