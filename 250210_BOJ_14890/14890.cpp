#include<iostream>

using namespace std;

const int MAX_N = 100;
int N, L;
int arr[MAX_N][MAX_N] = { 0, };

//경사로 설치 가능 여부 체크
bool slope(int check[MAX_N]) {
	bool taken[MAX_N] = { false }; // 경사로가 설치되어 있는지 체크
	for (int i = 0; i < N - 1; i++) {
		if (check[i] - check[i + 1] > 1 || check[i] - check[i + 1] < -1) // 경사로 아예 못 놓는 경우
			return false;

		// 차이가 1 나는 경우 
		// 1. 높아지는 경우 (왼쪽에 L개의 같은 높이 바닥 있어야 함)
		if (check[i + 1] - check[i] == 1) {
			if (i - L + 1 < 0) return false;
			for (int j = i; j > i - L; j--) {
				// 높이가 같지 않을 경우, 이미 경사로가 있는 경우 확인
				if (check[j] != check[i] || taken[j])
					return false;
				taken[j] = true;
			}
		}

		// 2. 낮아지는 경우 (오른쪽에 L개의 같은 높이 바닥 있어야 함)
		else if (check[i + 1] - check[i] == -1) {
			if (i + L >= N) return false;
			for (int j = i + 1; j < i + 1 + L; j++) {
				if (check[j] != check[i + 1] || taken[j])
					return false;
				taken[j] = true;
			}
		}
	}
	return true;
}

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> L;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (slope(arr[i]))
			cnt++;
	}
	for (int j = 0; j < N; j++) {
		int col[MAX_N];
		for (int i = 0; i < N; i++) {
			col[i] = arr[i][j];
		}
		if (slope(col))
			cnt++;
	}
	cout << cnt;
}
