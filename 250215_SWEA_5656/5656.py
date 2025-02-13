import sys
sys.stdin = open("sample_input.txt", 'r')
from collections import deque


# 구슬은 N번 쏠 수 있음
# 벽돌은 W x H 배열
# 벽돌은 숫자 1 ~ 9로 표현
# 상하좌우로 (벽돌 숫자 - 1) 칸이 함께 제거

# Brute Force
# 1 <= N <= 4
# 2 <= W <= 12
# 2 <= H <= 15
# 12 x 12 x 12 x 12 경우 -> 256 x 81 = 20,736


# 재귀 함수를 사용해서 n번 공 쏘기
# 최대로 벽돌을 부수는 경우를 return
# 남은 공 던지는 횟수 = r
# r = 0 -> return 0
# r = 1 -> return (r = 0 인 경우 + 1일 때 부순 벽돌) 최댓값
# r = 2 -> return (r = 1 인 경우 + 2일 때 부순 벽돌) 최댓값
# ... 이런식으로 순회하며 최대로 벽돌을 부순 경우를 찾는다
def simul(arr, n, w, h):
    if n <= 0: return 0
    M = 0
    q = deque()

    for shooting_point in range(w):
        temp = []

        for i in range(len(arr)):
            temp.append(arr[i][:])
        

        # 공이 맞는 지점 찾기
        hit = 0
        while temp[shooting_point][hit] == 0:
            hit += 1
            if hit >= h: break
				
				# 벽돌이 없으면 pruning
        if hit >= h: continue
				
        q.append((shooting_point, hit))
        visited = [(shooting_point, hit)]
				
				# 제거해야 하는 벽돌을 담는 집합
        remove = set()
        remove.add((shooting_point, hit))
				
				# Queue를 사용해서 공을 한번 던졌을 때, 부서지는 벽돌들 다 찾기
        while len(q) > 0:
            boom_x, boom_y = q.popleft()
            boom_range = temp[boom_x][boom_y]
						
						# 부서지는 벽돌들 탐색
            for i in range(1, boom_range):
		            # 상 / 하 / 좌 / 우  탐색
                down_x = boom_x - i
                up_x = boom_x + i
                left_y = boom_y - i
                right_y = boom_y + i

                if down_x >= 0:
                    if temp[down_x][boom_y] > 0:
		                    # 벽돌이 있으면 집합에 삽입
                        remove.add((down_x, boom_y))
                        # 벽돌이 1보다 큰 경우 -> 주변 벽돌도 부서지는 경우, Q에 삽입
                        if temp[down_x][boom_y] > 1:
                            if (down_x, boom_y) not in visited:
                                q.append((down_x, boom_y))
                                # 이미 삽입된 벽돌은 다시 삽입하지 않음
                                visited.append((down_x, boom_y))
                if up_x < w:
                    if temp[up_x][boom_y] > 0:
                        remove.add((up_x, boom_y))
                        if temp[up_x][boom_y] > 1:
                            if (up_x, boom_y) not in visited:
                                q.append((up_x, boom_y))
                                visited.append((up_x, boom_y))
                if left_y >= 0:
                    if temp[boom_x][left_y] > 0:
                        remove.add((boom_x, left_y))
                        if temp[boom_x][left_y] > 1:
                            if (boom_x, left_y) not in visited:
                                q.append((boom_x, left_y))
                                visited.append((boom_x, left_y))
                if right_y < h:
                    if temp[boom_x][right_y] > 0:
                        remove.add((boom_x, right_y))
                        if temp[boom_x][right_y] > 1:
                            if (boom_x, right_y) not in visited:
                                q.append((boom_x, right_y))
                                visited.append((boom_x, right_y))
        
        # len(remove) = 부서진 벽돌의 개수
        m = len(remove)
        # remove에 있는 (x, y) 좌표를 y의 내림차순으로 정렬
        # pop할 때, 작은 y부터 pop하면 이상한 값이 pop 될 수 있음
        remove = sorted(list(remove), key = lambda k: -k[1])

				# 삭제
        for i, j in remove:
            temp[i].pop(j)
				
				# 삭제한만큼 뒤에 0 추가
        for i, _ in remove:
            temp[i].insert(0, 0)
				
				# 재귀 함수를 돌면서 최댓값 찾기
        M = max(simul(temp, n-1, w, h) + m, M)

    return M

t = int(input())
for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    total = 0

		# arr을 전치 행렬로 저장
		# 벽돌 층을 보다 쉽게 접근하기 위함 (pop, insert)
    arr = [[] for i in range(w)]
    for i in range(h):
        line = list(map(int, input().split()))
        for j in range(len(line)):
            arr[j].append(line[j])
            if line[j] > 0: total += 1

    print(f"#{tc} {total - simul(arr, n, w, h)}")