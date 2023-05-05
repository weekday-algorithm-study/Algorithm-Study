"""
N과 M (4)
문제: https://www.acmicpc.net/problem/15652
"""

n, m = map(int, input().split())

res = []

def dfs(cnt):
    if cnt == m:
        print(*res)
        return

    for i in range(1, n+1):
        if not res or res[-1] <= i:
            res.append(i)
            dfs(cnt+1)
            res.pop()

dfs(0)