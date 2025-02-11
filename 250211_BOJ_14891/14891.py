import sys
input = sys.stdin.readline


# 마주한 A, B 톱니바퀴
# A는 시계 / 반시계로 회전
# A와 B의 마주한 극이 반대일 때, B는 A와 반대 방향으로 회전
# 극이 다를 경우 회전 안함

status = [[]]
index = [0 for i in range(5)]
for i in range(1, 5):
    status.append([])
    line = input().rstrip()

    for j in range(len(line)):
        status[i].append(int(line[j]))

k = int(input())
for _ in range(k):
    w, dir = map(int, input().split())

    current_dir = dir
    current_wheel = w

    # 좌측 탐색
    for next_wheel in range(current_wheel-1, 0, -1):
        left = status[current_wheel][(index[current_wheel] + 6) % 8]
        right = status[next_wheel][(index[next_wheel] + 2) % 8]

        if (left + right) % 2 == 1:
            current_dir = -current_dir
            current_wheel = next_wheel
        
        else: break

    # 톱니바퀴 다 돌려주기
    for i in range(current_wheel, w):
        index[i] = (index[i] + 8 - current_dir) % 8
        current_dir = -current_dir

    current_dir = dir
    current_wheel = w
    for next_wheel in range(current_wheel+1, 5):
        left = status[next_wheel][(index[next_wheel] +  6) % 8]
        right = status[current_wheel][(index[current_wheel] + 2) % 8]
        
        if (left + right) % 2 == 1:
            current_dir = -current_dir
            current_wheel = next_wheel
        
        else: break

    # 톱니바퀴 다 돌려주기
    for i in range(current_wheel, w, -1):
        index[i] = (index[i] + 8 - current_dir) % 8
        current_dir = -current_dir

    index[w] = (index[w] + 8 - dir) % 8

result = 0
for i in range(1, len(index)):
    result += status[i][index[i]] * (1 << (i-1))

print(result)