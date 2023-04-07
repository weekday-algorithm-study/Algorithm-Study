"""
두 배열의 합
문제: https://www.acmicpc.net/problem/2143
"""

import sys
from collections import Counter

input = sys.stdin.readline

# 입력받기

t = int(input())

n = int(input())

A = list(map(int, input().split()))

m = int(input())

B = list(map(int, input().split()))

# 정답
answer = 0

# 딕셔너리
dic = Counter()

for i in range(n):
    for j in range(i, n):
        # 배열 A의 모든 부배열의 합의 경우의 수를 딕셔너리에 저장
        dic[sum(A[i:j+1])] += 1

# 예시의 입력값으로 배열 A에서 나타날 수 있는 부배열합의 모든 경우의 수
# Counter({1: 2, 4: 2, 3: 2, 5: 1, 7: 1, 6: 1, 2: 1})

for i in range(m):
    for j in range(i, m):
        # 타켓 값에서 B의 부배열을 빼준 값
        tmp = t - sum(B[i:j+1])
        # 타겟 값에서 B의 부배열을 빼준 값이 딕셔너리에 있다면
        if tmp in dic:
            # 딕셔너리에 저장되어 있는 A 부배열의 합의 경우의 수를 answer에 더해주면 된다.
            answer += dic[tmp]

print(answer)