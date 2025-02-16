#include<iostream>
#include<vector>
#include<deque>
#include<algorithm>
#include <string>

using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    vector<deque<int>> dq(4, deque<int>(8));

    string s;
    int n, a, b;
    for (int i = 0; i < 4; i++) {
        cin >> s;
        for (int j = 0; j < 8; j++) {
            dq[i][j] = s[j] - '0';
        }
    }
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        a -= 1;
        vector<bool> shouldRotate(4, false);
        vector<int> dir(4, 0);

        shouldRotate[a] = true;
        dir[a] = b;

        for (int j = a; j > 0; j--) {
            if (shouldRotate[j] && dq[j][6] != dq[j - 1][2]) {
                shouldRotate[j - 1] = true;
                dir[j - 1] = -dir[j];
            }
        }
        for (int j = a; j < 3; j++) {
            if (shouldRotate[j] && dq[j][2] != dq[j + 1][6]) {
                shouldRotate[j + 1] = true;
                dir[j + 1] = -dir[j];
            }
        }
        for (int j = 0; j < 4; j++) {
            if (shouldRotate[j]) {
                if (dir[j] == 1) {
                    dq[j].push_front(dq[j].back());
                    dq[j].pop_back();
                }
                else if (dir[j] == -1) {
                    dq[j].push_back(dq[j].front());
                    dq[j].pop_front();
                }
            }
        }
    }
    int ans = 0;
    if (dq[0][0] == 1) ans += 1;
    if (dq[1][0] == 1) ans += 2;
    if (dq[2][0] == 1) ans += 4;
    if (dq[3][0] == 1) ans += 8;

    cout << ans << "\n";

    return 0;
}
