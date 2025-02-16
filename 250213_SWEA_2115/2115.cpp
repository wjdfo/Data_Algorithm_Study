from itertools import combinations

def getMaxforRow(arrRow, C) :
    maxProfit = 0
    M = len(arrRow)
    #모든 부분집합 탐색
    for i in range(1, M + 1) :
        for subset in combinations(arrRow, i) :
            if sum(subset) <= C : #그 중 C이하인 것만
                profit = sum(x * *2 for x in subset) #수익 계산
                maxProfit = max(maxProfit, profit)
                return maxProfit

                def getTotalMax(N, M, C, arr) :
                maxTotal = 0

                pos = [(r, c) for r in range(N) for c in range(N - M + 1)]
                for (r1, c1), (r2, c2) in combinations(pos, 2) :
                    if r1 == r2 : #겹치는 경우
                        continue

                        honey1 = arr[r1][c1:c1 + M]
                        honey2 = arr[r2][c2:c2 + M]
                        #각각의 일꾼에 대해서 최대 수익 계산해주기
                        profit1 = getMaxforRow(honey1, C)
                        profit2 = getMaxforRow(honey2, C)
                        #총 최대 수익 계산
                        maxTotal = max(maxTotal, profit1 + profit2)
                        return maxTotal

                        T = int(input())
                        for t in range(1, T + 1) :
                            N, M, C = map(int, input().split())
                            arr = [list(map(int, input().split()))for _ in range(N)]

                            ans = getTotalMax(N, M, C, arr)
                            print(f"#{t} {ans}")