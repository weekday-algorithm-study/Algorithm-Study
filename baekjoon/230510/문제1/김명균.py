"""
줄 세우기
문제: https://www.acmicpc.net/problem/2631
"""
import sys

input = sys.stdin.readline

# 아이들 수
n = int(input())

# 아이들 입력
nums = [int(input()) for _ in range(n)]

print(nums)