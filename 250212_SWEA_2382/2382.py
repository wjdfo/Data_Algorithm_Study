# 미생물격리
# k개의 미생물 군집
# n*n 사이즈의 배열, 테두리는 모두 약품처리
# k개 만큼의 군집에 대한 정보 제공 세로위치,가로위치,미생물수,이동방향
# 1시간 마다 지정된 상하좌우로 이동
# 미생물 군집이 약품이 칠해진 가장자리에 도착하면, 미생물 군집의 수가 //2되고, 이동방향이 반대로 바뀜
# 0이 될수도 있음 => 그런경우는 군집이 사라지게 됨.
# 이동후 두개이상이 되는 경우는 군집이 합쳐지는데, 미생물 수는 두 군집의 합, 이동방향은 더 큰수
# 위의 경우에는 무조건 대소가 확실한 경우만 제공
# m시간 이후 남아있는 미생물 수의 총합을 구하기
# 이동은 독립적!! 이동중에 겹치는 건 고려안하고, 이동을 다 했을때를 고려하기
# import sys
# sys.stdin = open('sample_input.txt')
# 상하좌우 방향 (0: 상, 1: 하, 2: 좌, 3: 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 미생물 이동 함수 (단순 이동만 수행)
def move():
    global visit  # visit 초기화
    visit = [[[] for _ in range(n)] for _ in range(n)]

    for x, y, num, d in info:
        nx, ny = x + dx[d], y + dy[d]

        # 경계에 도달하면 미생물 수 반감 및 방향 변경
        if nx == 0 or ny == 0 or nx == n - 1 or ny == n - 1:
            num //= 2
            d = {0: 1, 1: 0, 2: 3, 3: 2}[d]  # 방향 반대 전환

        # 미생물이 남아 있으면 새로운 위치에 추가
        if num > 0:
            visit[nx][ny].append((num, d))


# 같은 위치 미생물 합치는 함수
def check():
    global info
    new_info = []

    for i in range(n):
        for j in range(n):
            if len(visit[i][j]) > 0:  # 미생물이 존재하는 위치
                if len(visit[i][j]) == 1:  # 단일 군집이면 그대로 추가
                    new_info.append((i, j, visit[i][j][0][0], visit[i][j][0][1]))
                else:  # 여러 개의 군집이 하나의 칸에 모였을 경우
                    visit[i][j].sort(reverse=True, key=lambda x: x[0])  # 미생물 수 기준 정렬
                    total_sum = sum(num for num, _ in visit[i][j])  # 미생물 수 합산
                    max_d = visit[i][j][0][1]  # 가장 큰 미생물 군집의 방향 유지
                    new_info.append((i, j, total_sum, max_d))

    info = new_info  # info 갱신


# 최종 미생물 수 계산
def cal_res():
    return sum(num for _, _, num, _ in info)


tc = int(input())
for t in range(1,tc+1):
    n, m, k = map(int, input().split())  # 격자 크기(n), 격리 시간(m), 군집 개수(k)
    info = []

    for _ in range(k):
        x, y, num, d = map(int, input().split())
        info.append((x, y, num, d - 1))  # 방향을 0~3으로 변환

    # m시간 동안 시뮬레이션 실행
    for _ in range(m):
        move()  # 미생물 이동
        check()  # 군집 합치기 및 방향 재설정

    # 최종 미생물 수 출력
    print(f'#{t} {cal_res()}')

