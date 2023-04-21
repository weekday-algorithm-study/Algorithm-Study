"""
드래곤 앤 던전
문제: https://www.acmicpc.net/problem/16434
"""
import sys

input = sys.stdin.readline

# 방의 개수와 초기 공격력
n, attack = map(int, input().split())

for _ in range(n):
    # t=1 => 공격력이 a이고 생명력이 h인 몬스터
    # t=2 => 용사의 공격력을 a만큼 올려주고 생명력을 h만큼 올려주는 포션
    t, a, h = map(int, input().split())
