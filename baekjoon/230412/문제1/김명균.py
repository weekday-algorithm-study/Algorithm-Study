"""
동전 분배
문제: https://www.acmicpc.net/problem/1943
"""
import sys

input = sys.stdin.readline

for _ in range(3):

    n = int(input())

    # 돈의 총합
    total = 0

    # 동전 리스트
    coins = []

    # 입력 받기
    for _ in range(n):
        a, b = map(int, input().split())
        # 입력받으면서 총계구하기
        total += (a*b)
        coins.append([a, b])

    # 만약 총합이 홀수이면
    if total % 2 == 1:
        # 1 출력하고 다음으로
        print(0)
        continue

    # 총계의 절반을 가진 동전으로 만들 수 있어야 한다.
    half = total//2

    # dp 테이블
    dp = [1] + [0] * half

    for i in range(len(coins)):
        coin, cnt = coins[i]
        for j in range(half, coin-1, -1):
            if dp[j-coin]:
                for k in range(cnt):
                    if j+coin*k <= half:
                        dp[j+coin*k] = 1
                    else:
                        break

    print(dp[-1])

