"""
사과나무
문제: https://www.acmicpc.net/problem/20002
"""
import sys

input = sys.stdin.readline

# 과수원 크기 입력
n = int(input())

# 사과나물 입력
board = [list(map(int, input().split())) for _ in range(n)]

# 정답
answer = -sys.maxsize

# 크기 n인 정사각형의 총 이익
temp = 0
for i in range(n):
    for j in range(n):
        temp += board[i][j]

answer = max(answer, temp)




