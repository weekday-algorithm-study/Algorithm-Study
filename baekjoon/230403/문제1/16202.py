"""
MST 게임
문제: https://www.acmicpc.net/problem/16202
"""
import sys

input = sys.stdin.readline

# 입력받기
n, m, k = map(int, input().split())

# 간선
edges = []

# 간선 입력받기
for i in range(m):
    a, b = map(int, input().split())
    # 간선 테이블에 각 간선의 비용 저장
    edges.append((i+1, a, b))

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a==b:
        return False
    if a < b:
        parent[a] = b
        return True
    else:
        parent[b] = a
        return True


for i in range(k):
    # 부모 테이블
    parent = [0] * (n + 1)
    for j in range(1, n+1):
        parent[j] = j

    # 간선의 수
    cnt = 0

    # 각 턴의 정답
    total = 0

    for cost, a, b in edges[i:]:
        if union_parent(parent, a, b):
            total += cost
            cnt += 1
            if cnt == n-1:
                break
    if cnt == n-1:
        print(total, end=" ")
    else:
        print(0, end=" ")




