"""
사과나무
문제: https://www.acmicpc.net/problem/20002
"""
import sys

input = sys.stdin.readline

# 과수원 크기 입력
n = int(input())

# 누적합을 위한 2차월 배열 => ps[i][j] = [0,0] ~ [i][j]의 구간합
ps = [[-1001] * (n+1) for _ in range(n+1)]

# 구간합 구하기
for i in range(1, n+1):
    nums = list(map(int, input().split()))
    for j in range(1, n+1):
        ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + nums[j-1]

# 정답
answer = ps[0][0]

for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            temp = ps[i+k][j+k] - ps[i-1][j+k] - ps[i+k][j-1] + ps[i-1][j-1]
            answer = max(answer, temp)

print(answer)









