"""
계단 오르기
문제: https://www.acmicpc.net/problem/2579
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)


if n <= 2:
    if n == 1:
        print(nums[1])
    else:
        print(nums[1] + nums[2])
else:

    dp[1] = nums[1]
    dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])

    for i in range(3, n+1):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i - 1] + nums[i])

    print(dp[n])