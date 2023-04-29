"""
두 개의 배열
문제: https://www.acmicpc.net/problem/17124
"""
import sys

input = sys.stdin.readline

# 케이스
t = int(input())

# 이분탐색 함수
def binary_large(num, array, left, right):

    mid = (left + right) // 2
    # 찾는 값이 같다면 그대로 그 값 리턴
    if array[mid] == num:
        return array[mid]

    # 찾는 값이 더 작다면
    if num < array[mid]:
        return binary_large(num, array, left, mid)
    # 찾는 값이 더 크다면
    else:
        return binary_large(num, array, mid, right)


for _ in range(t):
    # 배열A, 배열B의 길이
    n, m = map(int, input().split())
    # 배열 A
    a = list(map(int, input().split()))
    # 배열 B
    b = list(map(int, input().split()))

    # 배열B 이분탐색을 위한 오름차순 정렬
    b.sort()

    # 정답
    answer = 0

    temp = sys.maxsize


