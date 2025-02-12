from collections import deque

def turn(cog, direction):
    '''
    톱니바퀴 회전 함수
    cog = 톱니바퀴 = 큐
          12시 방향부터 0 ~ 7
    direction = 회전 방향
                1 -> 시계, -1 -> 반시계
    시계 방향 회전 -> 꼬리 pop, 머리 append
    반시계 방향 회전 -> 머리 pop, 꼬리 append
    '''
    if direction == 1:
        cog.appendleft(cog.pop())
    else:
        cog.append(cog.popleft())
        
def check(cogs, magnatic):
    '''
    3곳의 접점 확인 함수
    톱니 바퀴의 왼쪽 접점 인덱스 = 6
    톱니 바퀴의 오른쪽 접점 인덱스 = 2
    왼쪽 바퀴 오른쪽 == 오른쪽 바퀴 왼쪽 -> False
    왼쪽 바퀴 오른쪽 != 오른쪽 바퀴 왼쪽 -> True
    '''
    check_left = 6
    check_right = 2
    for i in range(3):
        if cogs[i][check_right] != cogs[i + 1][check_left]:
            magnatic[i] = True
        else:
            magnatic[i] = False
            
'''
cogs = 톱니바퀴 배열
magnatic = 0-1, 1-2, 2-3 톱니바퀴 간 3개의 접점의 극성 확인
            False -> 같은 극, True -> 다른 극
dir = 각 톱니바퀴들의 회전 방향
'''
cogs = []
magnatic = [False, False, False]
dir = [0, 0, 0, 0]
for _ in range(4):
    cogs.append(deque(map(int, str(input()))))

check(cogs, magnatic)

n = int(input())
for _ in range(n):
    idx, direction = map(int, input().split())
    
    # 인덱스 -1 해서 편하게
    # 짝홀 같은 애들끼리 같은 방향으로 회전
    idx -= 1
    if idx % 2:
        dir[0] = -direction
        dir[2] = -direction
        dir[1] = direction
        dir[3] = direction
    else:
        dir[0] = direction
        dir[2] = direction
        dir[1] = -direction
        dir[3] = -direction
    
    # 처음 회전하는 바퀴의 오른쪽부터 확인
    # ex) 1번 회전하면 2, 3 확인
    # magnatic 확인해서 다른극이면 계속 회전, 다르면 break
    for i in range(idx, 3):
        if magnatic[i]:
            turn(cogs[i + 1], dir[i + 1])
        else:
            break
    # 처음 회전하는 바퀴의 왼쪽부터 확인
    # ex) 2번 회전하면 1, 0 확인
    # magnatic 확인해서 다른극이면 계속 회전, 다르면 break
    for i in range(idx - 1, -1, -1):
        if magnatic[i]:
            turn(cogs[i], dir[i])
        else:
            break
    # 처음 회전하는 바퀴 회전
    turn(cogs[idx], dir[idx])
    # 접점들 극성 재확인
    check(cogs, magnatic)
#결과 출력
print(cogs[0][0] + cogs[1][0] * 2 + cogs[2][0] * 4 + cogs[3][0] * 8)