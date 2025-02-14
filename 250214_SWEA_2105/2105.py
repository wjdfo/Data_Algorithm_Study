import sys
sys.stdin = open("sample_input.txt", 'r')

# 우하, 좌하, 좌상, 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

# x, y: 현재 위치, curve: 방향, visited: 방문한 카페
def course(x, y, curve, visited):
    global ans

    # 두 바퀴 돌은 경우 -> 사각형의 두 변이 그려짐 -> 사각형이 완성되어도 최대 길이는 현재까지의 두배
    # len(visited) * 2 < ans: 사각형의 예상 길이가 현재 최대 길이보다 작으면 가지치기
    if curve == 2 and ans > 2 * len(visited):
        return
    
    # curve > 3: 4번 이상 방향을 바꾼 경우 -> 사각형이 아닌 다각형이 그려짐
    if curve > 3:
        return
    
    # curve == 3: 3번 방향을 바꾸고
    # x, y: 시작점으로 돌아온 경우 -> 사각형이 완성됨
    # len(visited) > 3: 최소 4개를 방문해야 사각형
    if curve == 3 and x == start_x and y == start_y and len(visited) > 3:
        ans = max(ans, len(visited))
        return
    
    for i in range(curve, 4):
        # nx, ny: 다음 위치
        nx, ny = x + dx[i], y + dy[i]
        
        # 다음 위치가 범위 내에 있고, 방문한 카페가 아닌 경우
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in visited:
            # 방문한 카페 추가
            visited.add(arr[nx][ny])
            # 다음 위치로 이동
            course(nx, ny, i, visited)
            # 백트래킹
            visited.remove(arr[nx][ny])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            start_x, start_y = i, j
            course(i, j, 0, set())
    print(f'#{tc} {ans}')