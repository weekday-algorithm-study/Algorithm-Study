"""
뱀
문제: https://www.acmicpc.net/problem/3190
"""
import sys
from collections import deque

input = sys.stdin.readline

# 보드의 크기 입력
n = int(input())

# 보드 생성
board = [[0]*n for _ in range(n)]

# 사과의 개수 입력
k = int(input())

# 사과 위치 입력받기
for _ in range(k):
    a, b = map(int, input().split())

    # 보드에 사과 표시하기
    board[a-1][b-1] = 1

# 방향 전환 횟수 입력
c = int(input())

# 시간과 방향 정보 리스트
command = deque()

# 시간과 방향 정보 입력
for _ in range(c):
    time, direction = input().split()
    time = int(time)
    command.append([time, direction])

# 정답
answer = 0

# 시작 위치
start = [0, 0]

# 뱀
snake = deque([[0, 0]])


# 움직임
head = [0, 1]

while 1:
    answer += 1
    # 명령어가 있다면 실행
    if command:
        if answer == command[0][0]:
            temp = command.popleft()
            if temp[1] == "D":
                if head == [0, 1]:
                    head = [1, 0]
                elif head == [1, 0]:
                    head = [0, -1]
                elif head == [0, -1]:
                    head = [-1, 0]
                else:
                    head = [0, 1]
            else:
                if head == [0, 1]:
                    head =  [-1 ,0]
                elif head == [-1, 0]:
                    head = [0, -1]
                elif head == [0, -1]:
                    head = [1, 0]
                else:
                    head = [1, 0]

    start[0] += head[0]
    start[1] += head[1]

    if start[0] >= n or start[1] >= n or start[0] < 0 or start[1] < 0 or start in snake:
        break

    if board[start[0]][start[1]] == 1:
        snake.appendleft([start[0], start[1]])
    else:
        for x in snake:
            x[0] += head[0]
            x[1] += head[1]

    if snake[0][0] >= n or snake[0][1] >= n or snake[-1][0] >= n or snake[-1][1] >= n \
        or snake[0][0] < 0 or snake[0][1] < 0 or snake[-1][0] < 0 or snake[-1][1] < 0:
        break


print(answer)
