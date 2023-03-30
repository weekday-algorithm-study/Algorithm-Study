#include <iostream>
#include <algorithm> // min함수 

using namespace std;

int N;
int house[1001][3]; // DP테이블. house[i][j] = i번째 집의 색이 j일때의 최소비용 .
int cost[3]; // 비용

int main() {
	cin >> N;

	house[0][0] = 0;
	house[0][1] = 0;
	house[0][2] = 0;

	for (int i = 1; i <= N; i++) // 집은 1번부터 시작한다.
	{
		cin >> cost[0] >> cost[1] >> cost[2]; // RGB의 비용을 받아와 R=0 G=1 B=2에 저장한다.
		house[i][0] = cost[0] + min(house[i - 1][1], house[i - 1][2]); // ---------------------------------------------- //
		house[i][1] = cost[1] + min(house[i - 1][0], house[i - 1][2]); // 이전의 집의 색에서 더 작은 비용을 가져온다
		house[i][2] = cost[2] + min(house[i - 1][0], house[i - 1][1]); // ---------------------------------------------- //
	}

	cout << min(house[N][0], min(house[N][1], house[N][2])); // house[N]의 RGB중 가장 작은 비용을 출력한다.
	return 0;
}