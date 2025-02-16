#include <iostream>
#include <vector>

using namespace std;

struct INFO { // 행, 열, 미생물 수, 이동 방향 저장하는 구조체
    int r, c, num, dir;
};

// 상하좌우
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int reverse_dir(int dir) { // 방향 반전
    if (dir == 0) return 1;
    if (dir == 1) return 0;
    if (dir == 2) return 3;
    if (dir == 3) return 2;
    return -1;
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, M, K;
        cin >> N >> M >> K;

        vector<INFO> info(K);
        for (int i = 0; i < K; i++) {
            cin >> info[i].r >> info[i].c >> info[i].num >> info[i].dir;
            info[i].dir -= 1; // 방향을 0부터 시작하도록 변환
        }

        for (int i = 0; i < M; i++) {
            vector<vector<int>> grid(N, vector<int>(N, -1)); // 군집 위치 기록
            vector<vector<int>> max_num(N, vector<int>(N, 0)); // 최대 미생물 수 저장
            vector<INFO> next_info;

            for (int j = 0; j < info.size(); j++) {
                // 1. 이동
                info[j].r += dr[info[j].dir];
                info[j].c += dc[info[j].dir];

                // 미생물 수 줄어듦& 방향 바꾸기
                if (info[j].r == 0 || info[j].r == N - 1 || info[j].c == 0 || info[j].c == N - 1) {
                    info[j].num /= 2;
                    info[j].dir = reverse_dir(info[j].dir);
                }

                if (info[j].num > 0) {
                    int r = info[j].r, c = info[j].c;
                    int idx = grid[r][c];

                    // 해당 위치에 다른 군집이 없는 경우 -> 새로운 군집 추가
                    if (idx == -1) {
                        grid[r][c] = next_info.size();
                        max_num[r][c] = info[j].num; // 최대 미생물 수 기록
                        next_info.push_back(info[j]);
                    }
                    else {
                        // 이미 존재하는 군집이 있는 경우 -> 미생물 합치기
                        next_info[idx].num += info[j].num;

                        // 미생물 수가 가장 많았던 군집의 방향 유지
                        if (info[j].num > max_num[r][c]) {
                            max_num[r][c] = info[j].num;
                            next_info[idx].dir = info[j].dir;
                        }
                    }
                }
            }

            // 이동 후 미생물 정보 업데이트
            info = next_info;
        }

        // 총 미생물 수 계산
        int total = 0;
        for (int i = 0; i < info.size(); i++) {
            total += info[i].num;
        }

        cout << "#" << t << " " << total << "\n";
    }
    return 0;
}
