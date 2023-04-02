#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int>> egg(10);
bool visit;
int ans=0;

void dfs(int x) {  // 가장 왼쪽의 계란을 든다
	if (x == N) // 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우
	{
		int cnt = 0;
		for (int i = 0; i < N; i++)	{ if (egg[i].first <= 0) cnt++;	}
		ans = max(ans, cnt); // 현재 가지고 있는 깨진 계란의 수와 조금 전에 계산된 깨진 계란의 수를 비교함
		return;
	}

	if (egg[x].first <= 0) { dfs(x + 1); }
	else
	{
		visit = true;
		for (int i = 0; i < egg.size(); i++) // 3. 가장 최근에 든 계란 한칸 오른쪽 계란을 들고 2번을 반복한다.
		{
			if (x != i && egg[i].first > 0) // 2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중 하나를 친다.
			{
				visit = false;
				egg[x].first -= egg[i].second;
				egg[i].first -= egg[x].second;
				dfs(x + 1);
				egg[x].first += egg[i].second; // 원하는 답을 찾지 못했을 경우 원래 상태로 돌려놓음(백트래킹)
				egg[i].first += egg[x].second;
			}
		}
		if (visit) { dfs(N); } // 모든 계란이 깨져있다면 바로 종료(x==N이면 종료하므로)
	}
}

int main(void) {
	cin >> N;

	for (int i = 0; i < N; i++) {
		int S, W;
		cin >> S >> W;
		egg[i].first = S;
		egg[i].second = W;
	}

	dfs(0);

	cout << ans;

	return 0;
}