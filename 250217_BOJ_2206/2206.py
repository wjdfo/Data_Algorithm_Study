from collections import deque

dirs = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]

N, M = map(int, input().split())

# board[y][x] = 1: 벽, 0: 길
# z = 0: 벽을 부순 적이 없는 상태
# z = 1: 벽을 부순 적이 있는 상태
# visited[y][x][z] = y, x 좌표에 z 상태로 도달한 최단 거리
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
result = 9999999999

# BFS 탐색 용 큐 초기화
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

# 탐색 노드들을 queue에 넣어주면서 BFS 탐색
while queue:
    y, x, z = queue.popleft()

    # 도착 지점에 도달했을 때 최단 거리 갱신
    if y == N - 1 and x == M - 1:
        result = min(result, visited[y][x][z])

    # 상하좌우 탐색
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M:
            # 벽이고, 벽을 부순 적이 없는 상태인 경우
            if board[ny][nx] == 1 and visited[ny][nx][1] == 0 and z == 0:
                # 벽을 부수고 이동, visited 갱신
                # queue에 z = 1로 넣어줌
                visited[ny][nx][1] = visited[y][x][z] + 1
                queue.append((ny, nx, 1))
            # 벽이 아니고, 방문하지 않은 경우
            elif board[ny][nx] == 0 and visited[ny][nx][z] == 0:
                # 이동, visited 갱신
                visited[ny][nx][z] = visited[y][x][z] + 1
                queue.append((ny, nx, z))

# 최단 거리 출력
# result가 9999999999인 경우 도착 지점에 도달하지 못한 경우
if result == 9999999999:
    result = -1
print(result)