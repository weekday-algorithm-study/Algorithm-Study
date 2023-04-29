"""
전공책
문제: https://www.acmicpc.net/problem/16508
"""
import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline

# 만들고자 하는 단어
t = input().rstrip()

# 만들고자 하는 단어 딕셔너리
target_dic = Counter(t)

# 전공책의 개수
n = int(input())

# 전공책 입력
books = [list(input().split()) for _ in range(n)]

# 정답
answer = []

temp = target_dic

for i in range(1, n+1):
    comb = list(combinations(books, i))





