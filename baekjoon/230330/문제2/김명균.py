"""
RGB 거리
문제: https://www.acmicpc.net/problem/1149
"""

import sys

input = sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        nums[i][j] += min(nums[i-1][:j] + nums[i-1][j+1:])

print(min(nums[n - 1][0], nums[n - 1][1], nums[n - 1][2]))


