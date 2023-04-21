"""
중첩 집합 모델
문제: https://www.acmicpc.net/problem/19641
"""
import sys
from collections import deque

input = sys.stdin.readline

# 정점의 수
n = int(input())

# 그래프
graph = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(n):
    edge = list(map(int, input().split()))

    a = edge[0]

    for i in range(1, len(edge)-1):
        graph[a].append(edge[i])

# 정점
v = int(input())

# left, right 배열
answer = [[0]*2 for _ in range(n+1)]

# 루트 노드의 left는 항상 가장 작고 right는 항상 가장 크다.
answer[v][0] = 1
answer[v][1] = 2 * n

# 방문 리스트
visited = [0] * (n+1)

# 그래프 탐색
def bfs(start):
    left = answer[v][0]
    right = answer[v][1]
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        # 오름차순 방문을 해야 하므로 정렬
        graph[now].sort()

        for val in graph[now]:
            # 방문하지 않은 경우에
            if visited[val] == 0:
                # 방문 처리
                visited[val] = 1
                # left 증가
                left += 1
                # 증가된 left 표시
                answer[val][0] = left
                q.append(val)

bfs(v)

print(answer)