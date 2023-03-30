#include <iostream>
#include <algorithm> // min�Լ� 

using namespace std;

int N;
int house[1001][3]; // DP���̺�. house[i][j] = i��° ���� ���� j�϶��� �ּҺ�� .
int cost[3]; // ���

int main() {
	cin >> N;

	house[0][0] = 0;
	house[0][1] = 0;
	house[0][2] = 0;

	for (int i = 1; i <= N; i++) // ���� 1������ �����Ѵ�.
	{
		cin >> cost[0] >> cost[1] >> cost[2]; // RGB�� ����� �޾ƿ� R=0 G=1 B=2�� �����Ѵ�.
		house[i][0] = cost[0] + min(house[i - 1][1], house[i - 1][2]); // ---------------------------------------------- //
		house[i][1] = cost[1] + min(house[i - 1][0], house[i - 1][2]); // ������ ���� ������ �� ���� ����� �����´�
		house[i][2] = cost[2] + min(house[i - 1][0], house[i - 1][1]); // ---------------------------------------------- //
	}

	cout << min(house[N][0], min(house[N][1], house[N][2])); // house[N]�� RGB�� ���� ���� ����� ����Ѵ�.
	return 0;
}