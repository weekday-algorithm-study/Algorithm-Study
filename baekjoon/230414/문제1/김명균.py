import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

s, e = map(int, input().split())
INF = - sys.maxsize
distance = [INF] * (n+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [-INF, start])
    while q:
        now_cost, now = heapq.heappop(q)
        # 이미 최대 중량인 경우 무시
        if distance[now] > now_cost:
            continue

        for next_cost, next in graph[now]:
            cost = next_cost + now_cost
            if distance[next] < cost:
                distance[next] = cost
                heapq.heappush(q, [cost, next])

dijkstra(s)

print(distance)