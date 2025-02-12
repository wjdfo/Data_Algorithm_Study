import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    """
    N = 구역의 한변 길이
    M = 격리 시간
    K = 미생물 군집의 개수
    cells = 미생물 군집의 정보
            [x, y, 미생물 수, 이동 방향]
    collision = 충돌한 미생물 군집의 위치
    location = 해당 위치에 몇개의 미생물 군집의 수
    direction = 이동 방향
                [빈값, 상, 하, 좌, 우]
    """
    N, M, K = map(int, input().split())
    cells = []
    collision = set()
    location = [[0 for _ in range(N)] for _ in range(N)]
    direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 미생물 군집의 정보 입력
    # location에 미생물 군집의 수를 저장
    for i in range(K):
        cells.append(list(map(int, input().split())))
        location[cells[i][0]][cells[i][1]] += 1
    
    # 격리 시간만큼 반복
    for _ in range(M):
        # 나중에 제거할 미생물 군집
        cells_to_remove = []
        
        # 미생물 군집 이동
        for cell in cells:
            # 이동할거니까 현재 위치의 미생물 군집 수를 감소
            location[cell[0]][cell[1]] -= 1

            # 이동
            cell[0] += direction[cell[3]][0]
            cell[1] += direction[cell[3]][1]
            
            # 이동한 위치의 미생물 군집 수 증가
            location[cell[0]][cell[1]] += 1

            # 미생물 군집이 경계에 도착했을 때 방향 전환, 미생물 수 감소
            if cell[0] == 0:
                cell[3] = 2
                cell[2] = cell[2] // 2
            elif cell[1] == 0: 
                cell[3] = 4
                cell[2] = cell[2] // 2
            elif cell[0] == N - 1:
                cell[3] = 1
                cell[2] = cell[2] // 2
            elif cell[1] == N - 1:
                cell[3] = 3
                cell[2] = cell[2] // 2
            
            # 미생물 수가 0이 되면 제거할 미생물 군집에 추가
            if cell[2] == 0:
                location[cell[0]][cell[1]] -= 1
                cells_to_remove.append(cell)
        
        # 미생물 수가 0이 된 미생물 군집 제거
        for cell in cells_to_remove:
            cells.remove(cell)
        
        # 충돌한 미생물 군집 확인
        # 충돌한 미생물 군집은 location에 1보다 큰 값이 저장되어 있음
        for i in range(N):
            for j in range(N):
                if location[i][j] > 1:
                    collision.add((i, j))

        # 충돌한 미생물 군집이 있을 때
        while collision:
            # 충돌한 미생물 군집의 위치를 확인
            check = collision.pop()
            
            # 충돌한 미생물 군집을 저장할 배열
            merge = []
            
            # 충돌한 미생물 군집을 merge에 저장하고 cells에서 제거
            idx = 0
            cells_cnt = len(cells)
            while idx < cells_cnt:
                if cells[idx][0] == check[0] and cells[idx][1] == check[1]:
                    merge.append(cells.pop(idx))
                    cells_cnt -= 1
                    continue
                idx += 1
            
            # 미생물 수의 내림차순으로 정렬
            merge.sort(reverse=True, key=lambda x : x[2])
            # 미생물 수를 합쳐서 첫번째 미생물 군집에 저장
            # 첫번째 군집 => 미생물 수가 가장 많으므로 이동 방향은 첫번째 군집의 이동 방향
            merge[0][2] = sum([merging_cell[2] for merging_cell in merge])
            # 합쳐진 미생물 군집을 cells에 추가
            cells.append(merge[0])
            # 미생물 군집이 합쳐졌으므로 location을 1로 변경
            location[merge[0][0]][merge[0][1]] = 1

    print(f"#{tc}", sum([cell[2] for cell in cells]))