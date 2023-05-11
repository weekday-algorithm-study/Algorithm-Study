"""
숫자 야구
https://www.acmicpc.net/problem/2503
"""
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

# 가능한 숫자들 = 1~9 에서 중복이 없는 3가지 숫자 조합
nums = list(permutations([i for i in range(1, 10)], 3))

# nums의 크기
m = len(nums)

for _ in range(n):
    num, s, b = map(int, input().split())
    # 받은 숫자 리스트화
    num = list(str(num))





