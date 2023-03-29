#include <iostream>
#include <vector>									// vector 변수 선언
#include <algorithm>								// sort 함수(오름차순 정렬)
#include <cstring>									// memset 함수(초기화)

using namespace std;

#define MAX 10000 + 1								// N의 최대값 + 1

int N, M;
bool visit[MAX];									// DFS의 방문을 체크
vector<int> computer[MAX];							// 신뢰하는 컴퓨터 관계가 저장되어있음
int hack;											// DFS를 돌면서 해킹한 컴퓨터의 수를 체크

void dfs(int x)
{
	visit[x] = true;								// 방문 체크

	for (int i = 0; i < computer[x].size(); i++)
	{
		if (!visit[computer[x][i]]) {
			hack++;									
			dfs(computer[x][i]);					// 신뢰하고 있는 컴퓨터로 재귀
		}
	}

}

int main(void)
{
	cin >> N >> M;

	int a, b;
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b;
		computer[b].push_back(a);					// 두번째 변수(b)로 첫번째 변수(a)를 해킹할 수 있다.
	}												// 방향 그래프를 벡터로 연결 

	int cmax = 0;									// 해킹할 수 있는 컴퓨터 수의 최대값을 저장. 최대값만 필요하므로 이 문제는 DP가 아님.
	vector<int> ans;								// 가장 많은 컴퓨터를 해킹하는 컴퓨터의 번호를 저장.

	for (int i = 1; i <= N; i++)					// 해킹할 수 있는 컴퓨터는 0이 아니므로 변수 1부터 시작
	{
		memset(visit, false, sizeof(visit));		// DFS를 돌기 전에 방문 여부를 false로 초기화
		hack = 0;

		dfs(i);

		if (hack > cmax)							// DFS 돌고 얻은 '해킹할 수 있는 컴퓨터의 수'가 
		{											//				 '지금 가지고 있는 최대값'보다 크다면  
			ans.clear();							// 현재 가지고 있는 컴퓨터의 번호를 모두 지우고
			ans.push_back(i);						// 새로운 번호를 배열에 입력
			cmax = hack;							// 현재 가지고 있는 최대값을 갱신
		}
		else if (hack == cmax)						// DFS를 돌고 얻은 '해킹할 수 있는 컴퓨터의 수'가
		{											//				   '지금 가지고 있는 최대값'과 같다면
			ans.push_back(i);						// 새로운 번호를 배열에 추가
		}
	}

	sort(ans.begin(), ans.end());					// 오름차순 정렬
	for (int i = 0; i < ans.size(); i++)  cout << ans[i] << " ";

	return 0;
}