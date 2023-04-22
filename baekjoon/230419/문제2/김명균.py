"""
평행 우주
https://www.acmicpc.net/problem/17451
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# 지구
earth = nums[-1]

for i in range(n-2, -1, -1):
    # 행성의 속도보다 크다면
    if nums[i] < earth:
        if earth % nums[i] == 0:
            continue
        earth = ((earth // nums[i]) + 1) * nums[i]
    else:
        earth = nums[i]

print(earth)

