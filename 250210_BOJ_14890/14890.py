# n은 한변의 길이, l은 경사로의 길이
n, l = map(int, input().split())

# 지도 입력받고 카운트 초기화
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    # check = 경사로 설치 위치 확인 배열
    # 한 줄씩만 보면 되니까 매 줄 확인할때마다 초기화
    check = [True] * n
    
    # 한 줄씩 확인 시작
    for j in range(n):
        # 첫 칸에 cur 초기화
        if j == 0:
            cur = arr[i][j]

        # 이번칸이 이전칸과 다르다? 경사로 설치 가능한지 확인
        if arr[i][j] != cur:
            # 차이가 한 칸보다 크다? 설치 못하니 break
            if abs(arr[i][j] - cur) != 1:
                break
            
            # 한칸이면 설치 가능
            # 올라가는 경사로
            if arr[i][j] - cur == 1:
                # 혹시 경사로 설치하면 인덱스 벗어나나 확인
                if j - l >= 0:
                    # temp = 경사로 설치되는 칸들의 값
                    # ex) [2, 2] or [2, 3]
                    temp = [arr[i][j - step - 1] for step in range(l)]
                    # all(x == temp[0] for x in temp)
                    # temp에 들어있는 값이 모두 같은지? -> 경사로 설치가 가능한지?
                    # all(check[j - k - 1] for k in range(l))
                    # 경사로가 설치되는 칸에 이미 경사로가 설치된 적이 있는지?
                    if all(x == temp[0] for x in temp) and all(check[j - k - 1] for k in range(l)):
                        # 경사로 설치가능하니 설치되는 칸에 표시
                        for k in range(l):
                            check[j - k - 1] = False
                    # 이미 경사로가 설치된 칸에는 설치 안되니 break
                    else:
                        break
                # 경사로 설치하기에 부족한 공간이니 break
                else:
                    break

            # 내려가는 경사로
            elif arr[i][j] - cur == -1:
                # 혹시 경사로 설치하면 인덱스 벗어나나 확인
                if j + l <= n:
                    # temp = 경사로 설치되는 칸들의 값
                    # ex) [2, 2] or [2, 3]
                    temp = [arr[i][j + step] for step in range(l)]
                    # all(x == temp[0] for x in temp)
                    # temp에 들어있는 값이 모두 같은지? -> 경사로 설치가 가능한지?
                    # all(check[j + k] for k in range(l))
                    # 경사로가 설치되는 칸에 이미 경사로가 설치된 적이 있는지?
                    if all(x == temp[0] for x in temp) and all(check[j + k] for k in range(l)):
                        # 경사로 설치가능하니 설치되는 칸에 표시
                        for k in range(l):
                            check[j + k] = False
                    # 이미 경사로가 설치된 칸에는 설치 안되니 break
                    else:
                        break
                # 경사로 설치하기에 부족한 공간이니 break
                else:
                    break
        # cur 변경
        cur = arr[i][j]
        
        # 한 줄의 끝까지 왔으니 카운팅
        if j == n - 1:
            cnt += 1

# i, j만 바꿔서 나머지는 그대로
for i in range(n):
    check = [True] * n
    for j in range(n):
        if j == 0:
            cur = arr[j][i]

        if arr[j][i] != cur:
            if abs(arr[j][i] - cur) != 1:
                break
            
            if arr[j][i] - cur == 1:
                if j - l >= 0:
                    temp = [arr[j - step - 1][i] for step in range(l)]
                    if all(x == temp[0] for x in temp) and all(check[j - k - 1] for k in range(l)):
                        for k in range(l):
                            check[j - k - 1] = False
                    else:
                        break
                else:
                    break
            elif arr[j][i] - cur == -1:
                if j + l <= n:
                    temp = [arr[j + step][i] for step in range(l)]
                    if all(x == temp[0] for x in temp) and all(check[j + k] for k in range(l)):
                        for k in range(l):
                            check[j + k] = False
                    else:
                        break
                else:
                    break
                
        cur = arr[j][i]
        
        if j == n - 1:
            cnt += 1

print(cnt)