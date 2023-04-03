"""
계란으로 계란치기
문제:
"""

import sys

input = sys.stdin.readline

# 입력 받기
n = int(input())

eggs = []

# 입력 받기
for _ in range(n):
    eggs.append(list(map(int, input().split())))

# 정답
answer = 0

def dfs(idx, cnt):
    global answer

    # 마지막 계란까지 오면 재귀 종료
    if idx == n:
        answer = max(answer, cnt)
        return

    # 왼손에 든 계란이 깨지면 오른쪽 계란으로 넘어감
    if eggs[idx][0] <= 0:
        dfs(idx + 1, cnt)
    else: # 왼손의 계란으로 오른쪽 계란을 깼으면
        tmp = True
        for i in range(n):
            if i == idx: # 현재 계란이면 계속 반복함
                continue
            if eggs[i][0] > 0:
                tmp = False
                break

        if tmp: # 계란이 다 깨져있는 경우
            # 첫 번째 계란을 제외한 나머지 계란의 개수는 n-1 개
            answer = max(answer, n-1)

        for k in range(n):
            if k == idx or eggs[i][0] <= 0:
                continue
            # 계란 깨는 과정
            eggs[idx][0] -= eggs[k][1]
            eggs[k][0] -= eggs[idx][0]
            dfs(idx + 1, cnt)
            eggs[idx][0] += eggs[k][1]
            eggs[k][0] += eggs[idx][0]

dfs(0)

print(answer)