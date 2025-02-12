n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def solve(lst,v):
    #lst[1]부터 시작해서 전의 값과 cnt를 비교하기
    cnt = 1 # 이미 lst[0]이 하나 있으니까 그거 갯수는 기본값으로 깔아줌
    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            #같은경우
            cnt += 1
        elif lst[i-1] > lst[i]:
            #내려가는 경우
            cnt = 1
        elif lst[i-1] + 1 == lst[i] and cnt >= l and v[i-l:i]==[0]*l:
            #1증가하는 경우
            #위의 세조건이 만족하면 경사로를 놓을 수 있음.
            cnt = 1
            v[i-l] = [1]*l
        else:
            return False
    return True
        

res = 0
for lst in arr:
    v = [0]*len(lst)
    #한 행에 대해 정방향으로 탐색한것과, 반대 방향으로 탐색한 결과가 모두 true면 해당 행은 길이 될 수 있는 것.
    if solve(lst,v) and solve(lst[::-1],v[::-1]):
        res += 1

#전치행렬 -> 위에서 행한줄에 대해 갯수를 셌으니 이제 한 열에 대해 갯수를 세보면 됨
arr = list(map(list,zip(*arr)))
for lst in arr:
    v = [0]*len(lst)
    if solve(lst,v) and solve(lst[::-1],v[::-1]):
        res += 1
         
print(res)