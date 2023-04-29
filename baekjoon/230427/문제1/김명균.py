"""
미세먼지 안녕!
문제: https://www.acmicpc.net/problem/17144
"""
import sys

input = sys.stdin.readline

# 행, 열, 시간
r, c, t = map(int, input().split())

# 보드
board = [list(map(int, input().split())) for _ in range(r)]

# 미세먼지 확산 방향(위, 오른쪽, 아래, 왼쪽)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 공기 청정기 위치
cleaner1, cleaner2 = [0, 0], [0, 0]

for i in range(r):
    if board[i][0] == -1:
        cleaner1[0] = i
        cleaner2[0] = i+1
        break

# 미세먼지 확산 함수
def spread():
    for i in range(r):
        for j in range(c):
            # 미세먼지가 있는 칸인 경우
            if board[i][j] != -1 and board[i][j] != 0:
                # 남은 미세먼지 양을 계산하기 위한 변수
                temp = 0
                # 인접한 네 방향으로
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 보드판 내에 있고, 공기 청정기가 있는 곳이 아니라면
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        # 주변 방향으로 미세먼지를 확산하고
                        board[nx][ny] += board[i][j]//5
                        # 확산한 방향의 수만큼 temp에 더해준다.
                        temp += board[i][j]//5
                # 확산한 미세먼지 만큼 빼준다.
                board[i][j] -= temp

spread()
print(board)

