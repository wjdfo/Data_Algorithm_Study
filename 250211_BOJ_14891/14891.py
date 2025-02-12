#톱니바퀴
#4개의 톱니바퀴니까 5줄의 8칸을 만들어줌. 0줄은 사용하지않고 그냥 인덱스를 입력받은 그대로하기위해서임.
n = 4
arr = [[0]*8] + [list(map(int,input())) for _ in range(n)]
point = [0]*(n+1)      #1~4번까지 12시방향인 top을 정해줌. -> 얘로 나중에 점수매김+얘안에 0~8번인덱스값이 들어감. 얘는 그냥 포인터라고 생각.
k = int(input())

for _ in range(k):
    #1~4번중 움직일 톱니번호와 시계,반시계 방향.
    idx,dr = map(int,input().split())
    #얘는 회전해야할 톱니바퀴번호랑 회전할 방향을 넣을 리스트.
    tlist = [(idx,0)]
    #명령 대상으로 들어온 애는 무조건 회전함으로 무조건 넣음. idx가 홀수번이면 한칸뛰고 반대방향으로 돌면 idx+2번째는 회전하면 idx와 같은방향으로 돌게됨.
    #그렇기에 현재 회전을 명령받은 애와 2칸 순서가 차이가 나면 같은방향인 0이 들어가고 1칸 및 3칸 차이면 1이 들어갈것임.
    #tlist.append((idx,0))
    #해당 명령받은 톱니에서 오른쪽방향 탐색. 극이 같으면 멈추고, 극이 다르면 같은 극이 나올때까지 다음 톱니도 계속해서 돌려야함.
    for i in range(idx+1,n+1):
        if arr[i-1][(point[i-1]+2)%8] != arr[i][(point[i]+6)%8]:
            #왼쪽바퀴와 오른쪽바퀴가 극이 다르면 계속 회전함. 왼쪽바퀴일때는 3시방향값(12시방향부터 +2칸), 오른쪽바퀴일때는 9시방향값(12시방향부터 +6칸)
            tlist.append((i,abs(i-idx)%2))
        else:
            #극이 같다면 오른쪽 회전은 그만하고 멈춤
            break
    #왼쪽방향탐색 (현재명령받은 바퀴의 한칸전부터 1번까지니까)
    for i in range(idx-1,0,-1):
        if arr[i][(point[i]+2)%8] != arr[i+1][(point[i+1]+6)%8]:
            tlist.append((i,abs(idx-i)%2))
        else:
            break
    #다 탐색했으니 실제로 이동하기.
    for num,move in tlist:
        if move == 0:
            #명령받은 idx와 같은방향으로 point이동시켜줌.근데 이동은 시계방향일때 포인터는 거꾸로 - 하게 되니까 -dr을 해줘야함.
            #현재포인터값에서 dr만큼 한칸 이동하기.
            point[num] = (point[num]-dr+8)%8
        else:
            #얘는 반대방향임.
            point[num] = (point[num]+dr+8)%8


#계산은 point가 다 12시방향만 저장되어있기때문에 얘로 맞춰줘야함.
summ = 0
mul = [0,1,2,4,8]
for i in range(1,n+1):
    summ += arr[i][point[i]]*mul[i]
print(summ)