"""
N과 M(5)
문제: https://www.acmicpc.net/problem/15654
"""
n, m = map(int, input().split())

# 입력받고 정렬
nums = sorted(list(map(int, input().split())))

# 방문여부
visited = [0]*n

# 출력을 위한 배열
res = []

def dfs(cnt):
    # res에 담긴 수의 개수가 m개가 되면 출력
    if cnt == m:
        print(*res)
        return

    for i in range(n):
        # res에 없는 수면
        if visited[i] == 0:
            # index로 방문 체크하고
            visited[i] = 1
            # res에 넣고
            res.append(nums[i])
            # 재귀적으로 실행
            dfs(cnt + 1)
            # 재귀 끝나면 방문 체크 풀어주고 res에서 숫자를 빼준다.
            visited[i] = 0
            res.pop()


dfs(0)