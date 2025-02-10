import sys
input = sys.stdin.readline


def sol(arr):
    result = 0

    for i in range(len(arr)):
        flag = True
        prev = arr[i][0]
        left = False
        count = 1

        for j in range(1, len(arr[i])):
            if prev != arr[i][j]:

                if abs(prev - arr[i][j]) > 1:
                    flag = False
                    break
                
                # 이전 길에 left 경사로 설치해야 하는 경우
                if left == True:
                    if count < l:
                        flag = False
                        break
                    count -= l
                    left = False

                # 좌측에 경사로 설치해야 하는 경우
                if prev > arr[i][j]:
                    left = True
                
                # 우측에 경사로 설치해야 하는 경우
                elif prev < arr[i][j]:
                    if count < l:
                        flag = False
                        break
                    left = False

                prev = arr[i][j]
                count = 1

            # 이전 값과 같은 경우
            else: count += 1

        # 마지막 부분 경사로 추가
        if left == True and count < l: flag = False
        if flag: result += 1
    return result

n, l = map(int, input().split())

arr = []
arr_transpose = [[] for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        arr_transpose[j].append(arr[i][j])

print(sol(arr) + sol(arr_transpose))