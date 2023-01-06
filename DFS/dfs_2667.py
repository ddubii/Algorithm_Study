import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]  #상하좌우
    visited[x][y] = 1
    global mini_count
    for i in range(4):
        nowx, nowy = x + dx[i], y + dy[i]
        if 0 <= nowx < N and 0 <= nowy <N and graph[x][y] == graph[nowx][nowy] and visited[nowx][nowy] == 0:
            dfs(nowx, nowy)
            mini_count += 1


N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == '0':
            visited[i][j] = '1'

mini = []
for i in range(N):
    for j in range(N):
        mini_count = 0
        if visited[i][j] == 0:
            cnt += 1
            dfs(i,j)
            mini.append(mini_count+1)

print(cnt)
mini.sort()
for x in mini:
    print(x)


