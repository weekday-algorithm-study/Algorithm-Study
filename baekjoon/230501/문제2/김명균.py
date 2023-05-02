"""
N과 M(8)
문제: https://www.acmicpc.net/problem/15657
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

res = []

def dfs(level):
    if len(res) == m:
        print(*res)
        return
    for i in range(level, n):
        res.append(nums[i])
        dfs(i)
        res.pop() 
dfs(0)