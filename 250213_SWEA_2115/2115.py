import sys
sys.stdin = open("sample_input.txt", 'r')
from itertools import combinations


# N x N개의 벌통, 정사각형
# 벌꿀을 최대한 많이 채취해 최대 수익
# 두 명의 일꾼
# 각 일꾼은 가로로 연속된 M개의 벌통을 선택하고 채취
# 두 일꾼이 선택한 벌통은 서로 겹치면 안됨
# 서로 다른 벌통에서 채취한 꿀이 섞이면 상품 가치 하락
# -> 한 벌통에서 채취한 꿀은 하나의 용기에 담기
# 두 일꾼이 채취할 수 있는 꿀의 최대 양은 C
# 한 벌통에서 채취할 때 일부만 채취 불가능

# 벌통의 가치 = 벌통에 있는 꿀 ** 2

t = int(input())
for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    combination = []
    
    for i in range(1, m+1):
        for element in combinations(range(m), i):
            combination.append(element)

    arr = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        
        for j in range(0, len(line) - m + 1):
            Max = 0
            # line[j:j+m]에서 가장 큰 값 선택하기
            # 모든 조합
            for comb in combination:
                total = 0
                square_total = 0
                for index in comb:
                    total += line[j+index]
                    if total > c:
                        break
                    square_total += line[j+index] ** 2

                Max = max(square_total, Max)

            arr[i].append(Max)

    M = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            honey1 = arr[i][j]

            for x in range(i, len(arr)):
                for y in range(len(arr[x])):
                    if x == i and y < j + m: continue
                    honey2 = arr[x][y]
                    M = max(M, honey1 + honey2)

    print(f"#{tc} {M}")