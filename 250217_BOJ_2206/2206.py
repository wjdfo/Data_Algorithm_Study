dirs = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]


def dfs(cur, path, broken):
    global arr, visited, result
    
    if cur == (n - 1, m - 1):
        result = min(result, path)
        return

    for dir in dirs:
        nx, ny = cur[0] + dir[0], cur[1] + dir[1]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if arr[nx][ny]:
                if broken:
                    continue
                else:
                    visited[nx][ny] = 1
                    dfs((nx, ny), path + 1, 1)
                    visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                dfs((nx, ny), path + 1, broken)
                visited[nx][ny] = 0

n, m = map(int, input().split())

arr = [list(map(int, str(input()))) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

visited[0][0] = 1
result = 999999999
dfs((0, 0), 0, 0)

if result == 999999999:
    result = -1
else:
    result += 1
print(result)