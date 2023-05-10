"""
불!
문제: https://www.acmicpc.net/problem/4179
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

# 미로 입력
board = [list(input().rstrip()) for _ in range(r)]

# 지훈이 위치
start = [0, 0]

for i in range(r):
    for j in range(c):
        if board[i][j] == "J":
            start[0], start[1] = i, j
            break

# 불의 위치
fire = []

for i in range(r):
    for j in range(c):
        if board[i][j] == "F":
            fire.append([i, j])

# 지훈 방문여부
person_visited = [[0]*c for _ in range(r)]

# 불 방문여부
fire_visited = [[0]*c for _ in range(r)]

# 4 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    person_visited[x][y] = 1

    fire_q = deque(fire)
    for a, b in fire_q:
        fire_visited[a][b] = 1

    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != "#" and person_visited[nx][ny] == 0:
                    person_visited[nx][ny] = person_visited[now[0]][now[1]] + 1
                    q.append([nx, ny])
            else:
                return person_visited[now[0]][now[1]]

    while fire_q:
        f_x, f_y = fire_q.popleft()
        for i in range(4):
            fx = f_x + dx[i]
            fy = f_y + dy[i]
            if 0 <= fx < r and 0 <= fy < c and fire_visited[fx][fy] == 0 and board[fx][fy] != "#":
                fire_visited[fx][fy] = 1
                fire_q.append([fx, fy])

    return "IMPOSSIBLE"



print(bfs(start[0], start[1]))


