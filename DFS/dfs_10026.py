import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]  #상하좌우
    visited[x][y] = 1

    for i in range(4):
        nowx, nowy = x + dx[i], y + dy[i]

        if 0 <= nowx < N and 0 <= nowy <N and graph[x][y] == graph[nowx][nowy] and visited[nowx][nowy] == 0:
            dfs(nowx, nowy)


N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt1 += 1
            dfs(i,j)

for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = 'G'

cnt2 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(i,j)


print(cnt1, cnt2)