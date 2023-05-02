"""
배열 돌리기4
문제: https://www.acmicpc.net/problem/17406
"""
import sys

input = sys.stdin.readline

# 행, 열, 연산횟수 입력
n, m, k = map(int, input().split())

# 보드판 입력
board = [list(map(int, input().split())) for _ in range(n)]

# 연산 입력
op = [list(map(int, input().split())) for _ in range(k)]

# 배열회전
def rotate(r, c, s, board):
    # 정사각형의 왼쪽 위쪽
    start = [r-s-1, c-s-1]
    # 정사각형의 오른쪽 아래
    end = [r+s-1, c+s-1]

    # 종료조건 = start와 end의 중심이 되었을 때 stop
    condition = [(start[0]+end[0])//2, (start[1]+end[1])//2]

    # 회전방향 = [오른쪽, 아래쪽, 왼쪽, 위쪽]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    # 현재 위치의 값과 방향
    now, dir = 0, 0

    # 시작위치의 인덱스
    x, y = start

    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]

        # start 위치로 오게되면 멈춘다.
        if x == start[0] and y == start[1]:
            break

        # 보드판을 벗어나게 되면 방향을 바꿔야한다.
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            dir += 1
            continue

        # 값 변경
        board[x][y], now = now, board[x][y]

        x, y = nx, ny
    return board

print(rotate(op[0][0], op[0][1], op[0][2], board))

print(board)