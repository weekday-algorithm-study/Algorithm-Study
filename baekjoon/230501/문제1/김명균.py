"""
수강과목
문제: https://www.acmicpc.net/problem/17845
"""
import sys

input = sys.stdin.readline

# 최대공부시간, 과목 수
n, k = map(int, input().split())

# 과목 입력
subjects = [[0, 0]] + [list(map(int, input().split())) for _ in range(k)]

# dp 테이블
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, k+1):
    weight, time = subjects[i][0], subjects[i][1]
    for j in range(1, n+1):
        # 최대공부시간보다 필요공부시간이 더 크다면
        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-time] + weight, dp[i-1][j])

print(dp[k][n])




