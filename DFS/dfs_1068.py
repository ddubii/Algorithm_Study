#dfs_트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


node = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 삭제하는 노드 번호 = v이면 arr[v] 삭제
# arr[?] = v 이면 arr[?]의 부모 노드는 v 이다.
# 따라서 v를 제거하면

def dfs(v):
    arr[v] = -2  # 노드 지우기 표시
    for i in range(len(arr)):
        if v == arr[i]:  # 삭제된 노드를 부모 노드로 하는 경우
            dfs(i)  # 해당 노드 삭제, 딸린 노드 삭제 반복


dfs(x)
cnt = 0

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)
