import sys
sys.stdin = open("sample_input.txt", 'r')

def get_max_honey(available_hive, index, sum, sum_power_honey):
    """
    
    available_hive: 현재 선택 가능한 벌통
    index: 현재 선택한 벌통의 인덱스
    sum: 현재 선택한 벌통의 꿀의 양
    sum_power_honey: 현재 선택한 벌통의 꿀의 양의 제곱의 합 = 꿀의 가치
    M: 선택할 수 있는 벌통의 개수 = available_hive의 길이
    C: 선택할 수 있는 벌통의 꿀의 최대 양
    temp_max_honey: 현재 선택한 벌통의 꿀의 가치 중 최대값
    """
    global M, C, temp_max_honey
    
    # 현재 선택한 벌통의 꿀의 양이 C를 넘어가면 검사
    # 현재 선택한 벌통의 꿀의 꿀의 가치가 temp_max_honey보다 크면 갱신
    if sum <= C:
        temp_max_honey = max(temp_max_honey, sum_power_honey)
    # 현재 선택 가능한 벌통을 모두 선택했으면 종료
    if index == M:
        return
    
    # 현재 벌통 선택
    get_max_honey(available_hive, index + 1, sum + available_hive[index], sum_power_honey + available_hive[index] ** 2)
    # 현재 벌통 선택 x
    get_max_honey(available_hive, index + 1, sum, sum_power_honey)

T = int(input())

"""
N: 벌통의 한 변의 길이
M: 선택할 수 있는 벌통의 개수
C: 선택할 수 있는 벌통의 꿀의 최대 양
beehive: 벌통의 배열
max_honey: 벌통의 꿀의 가치의 최대값을 저장하는 배열
           max_honey[i][j]: i행 j열부터 M개의 벌통을 선택했을 때의 꿀의 가치의 최대값
"""
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]
    max_honey = [[0] * (N - M + 1) for _ in range(N)]
    
    # 각 벌통의 꿀의 가치의 최대값을 구함
    # max_honey[i][j] = i행 j열부터 M개의 벌통을 선택했을 때의 꿀의 가치의 최대값
    for i in range(N):
        for j in range(N - M + 1):
            temp_max_honey = 0
            get_max_honey(beehive[i][j:j + M], 0, 0, 0)
            max_honey[i][j] = temp_max_honey

    available_honey = []
    # 두 일꾼이 서로 겹치지 않는 경우
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(i, N):
                for l in range(N - M + 1):
                    if i == k and l - j < M:
                        continue
                    available_honey.append(max_honey[i][j] + max_honey[k][l])
    print(f'#{test_case} {max(available_honey)}')