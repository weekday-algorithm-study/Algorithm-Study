#include <iostream>
#include <vector>									// vector ���� ����
#include <algorithm>								// sort �Լ�(�������� ����)
#include <cstring>									// memset �Լ�(�ʱ�ȭ)

using namespace std;

#define MAX 10000 + 1								// N�� �ִ밪 + 1

int N, M;
bool visit[MAX];									// DFS�� �湮�� üũ
vector<int> computer[MAX];							// �ŷ��ϴ� ��ǻ�� ���谡 ����Ǿ�����
int hack;											// DFS�� ���鼭 ��ŷ�� ��ǻ���� ���� üũ

void dfs(int x)
{
	visit[x] = true;								// �湮 üũ

	for (int i = 0; i < computer[x].size(); i++)
	{
		if (!visit[computer[x][i]]) {
			hack++;									
			dfs(computer[x][i]);					// �ŷ��ϰ� �ִ� ��ǻ�ͷ� ���
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
		computer[b].push_back(a);					// �ι�° ����(b)�� ù��° ����(a)�� ��ŷ�� �� �ִ�.
	}												// ���� �׷����� ���ͷ� ���� 

	int cmax = 0;									// ��ŷ�� �� �ִ� ��ǻ�� ���� �ִ밪�� ����. �ִ밪�� �ʿ��ϹǷ� �� ������ DP�� �ƴ�.
	vector<int> ans;								// ���� ���� ��ǻ�͸� ��ŷ�ϴ� ��ǻ���� ��ȣ�� ����.

	for (int i = 1; i <= N; i++)					// ��ŷ�� �� �ִ� ��ǻ�ʹ� 0�� �ƴϹǷ� ���� 1���� ����
	{
		memset(visit, false, sizeof(visit));		// DFS�� ���� ���� �湮 ���θ� false�� �ʱ�ȭ
		hack = 0;

		dfs(i);

		if (hack > cmax)							// DFS ���� ���� '��ŷ�� �� �ִ� ��ǻ���� ��'�� 
		{											//				 '���� ������ �ִ� �ִ밪'���� ũ�ٸ�  
			ans.clear();							// ���� ������ �ִ� ��ǻ���� ��ȣ�� ��� �����
			ans.push_back(i);						// ���ο� ��ȣ�� �迭�� �Է�
			cmax = hack;							// ���� ������ �ִ� �ִ밪�� ����
		}
		else if (hack == cmax)						// DFS�� ���� ���� '��ŷ�� �� �ִ� ��ǻ���� ��'��
		{											//				   '���� ������ �ִ� �ִ밪'�� ���ٸ�
			ans.push_back(i);						// ���ο� ��ȣ�� �迭�� �߰�
		}
	}

	sort(ans.begin(), ans.end());					// �������� ����
	for (int i = 0; i < ans.size(); i++)  cout << ans[i] << " ";

	return 0;
}