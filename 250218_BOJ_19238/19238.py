from collections import deque
import heapq


def bfs(start_x, start_y, end_x, end_y):
    
    visit = [[999999999999] * (N + 1) for _ in range(N + 1)]
    visit[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))
    
    while queue:
        cur = queue.popleft()
        
        if cur[0] == end_x and cur[1] == end_y:
            break
        if fuel == 0:
            break
        
        for dir in dirs:
            nx, ny = dir[0] + cur[0], dir[1] + cur[1]
            if 0 < nx <= N and 0 < ny <= N and visit[nx][ny] > visit[cur[0]][cur[1]] + 1 and area[nx][ny] == 0:
                visit[nx][ny] = visit[cur[0]][cur[1]] + 1
                queue.append((nx, ny))
    
    return visit[end_x][end_y] if visit[end_x][end_y] != 999999999999 else -1


def distance():
    global passengers
    
    for passenger in passengers:
        passenger[4] = bfs(start[0], start[1], passenger[0], passenger[1])

    passengers.sort(reverse=True, key=lambda x : (x[4], x[0], x[1]))



dirs = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
)

N, M, fuel = map(int, input().split())
area = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    area[i] = [0] + list(map(int, input().split()))
start = list(map(int, input().split()))

passengers = [list(map(int, input().split())) + [0] for _ in range(M)]

while passengers:
    distance()
    target_passenger = passengers.pop()
    
    needed_fuel = target_passenger[4]
    if needed_fuel > fuel or fuel == -1 or needed_fuel == -1:
        fuel = -1
        break
    else:
        fuel -= needed_fuel
    
    needed_fuel = bfs(target_passenger[0], target_passenger[1], target_passenger[2], target_passenger[3])
    if needed_fuel > fuel or fuel == -1 or needed_fuel == -1:
        fuel = -1
        break
    else:
        fuel += needed_fuel
        start = (target_passenger[2], target_passenger[3])
    
print(fuel)