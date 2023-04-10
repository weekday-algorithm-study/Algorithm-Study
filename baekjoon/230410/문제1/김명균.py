"""
소풍
문제: https://www.acmicpc.net/problem/2026
"""
import sys

input = sys.stdin.readline

k, n, f = map(int, input().split())

graph = [[] for _ in range(n+1)]

friend = [[0]*(n+1) for _ in range(n+1)]

degree = [0] * (n+1)

for _ in range(f):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    friend[a][b], friend[b][a] = 1, 1
    degree[a] += 1
    degree[b] += 1




flag = False


def dfs(x, level, nums):
    if level == k:
        for num in nums:
            print(num)
        sys.exit(0)

    for i in range(x+1, n+1):
        if visited[i] == 0:
            for num in nums:
                if num not in graph[i]:
                    break
                visited[i] = 1
                dfs(i, nums + [i])



# 방문 여부 확인
visited = [0] * (n+1)

for i in range(1, n+1):
    if degree[i] < k-1: # 본인 포함 차수가 k보다 작으면 볼 필요X
        continue

    visited[i] = 1





