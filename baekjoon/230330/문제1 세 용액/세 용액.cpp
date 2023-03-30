#include <iostream>
#include <vector>
#include <algorithm> // sort �Լ�

using namespace std;

int N; // N�� �ִ�ġ�� 5000�̹Ƿ� int�� ����.
long long small = 3000000000 + 1; // ����� Ư���� �ִ�ġ 1,000,000,000�� 3�� �ߺ��� �� �����Ƿ� �ִ�ġ�� 3,000,000,000 + 1�� �ʱ�ȭ
vector<long long> answer(3); // �ּҰ��� ����� ����� Ư�� 3���� ������ vector ����. Ư���� �ִ�ġ�� 1,000,000,000�̹Ƿ� long long���� ����.

int main(void)
{
	cin >> N;

	vector<long long> liquid(N); // �־����� ����� Ư������ ������ vector ����. Ư�����̹Ƿ� long long
	for (int i = 0; i < N; i++) // N���� �ݺ��� i�� int�� �����ص� ������
	{
		cin >> liquid[i];
	}
	sort(liquid.begin(), liquid.end()); // �޾ƿ� ����� Ư������ ������������ ����

	// ---------------------------------------------------------------------------------------
	// 
	// ������������ ���ĵ� ����� �迭���� ���� ���� i�� ù��° num���� ����
	// num�� ������Ų ���·� left�� right �ΰ��� �����͸� ������ �ּҰ��� Ž���Ұ���
	// 
	// ---------------------------------------------------------------------------------------

	for (int i = 0; i < N; i++) {
		int num = i; // left�� right�� �����ϴ� ���� ������ ���� ������ ���� num
		int left = i; // �׻� �迭�� ���� ���� ���� �迭�� left �����ͷ� �ʱ�ȭ
		int right = N - 1; // �׻� �迭�� ���� ������ ���� right �����ͷ� �ʱ�ȭ

		while (left != right)
		{
			if (left == i) { left++; continue; } // ���� left�� num�� ���� ���¶�� �Ʒ� ������ ��ŵ�ϰ� �������� �ѱ�
			if (right == i) { right--; continue; } // ���� right�� num�� ���� ���¶�� �Ʒ� ������ ��ŵ�ϰ� �������� �ѱ�

			long long sum = liquid[left] + liquid[right] + liquid[num]; // �� ����� ��

			if (abs(sum) < small) // ������ �����ϸ�, 0�� ���� ����� ���� ã�� �����Ƿ� ���밪(abs)���� ���ؾ���
			{								// ���� sum�� ���밪�� ���� ������ �ִ� �ּҰ����� �� �۴ٸ�
				small = abs(sum);			// ���� ������ �ִ� �ּҰ��� sum�� ���밪���� ����
				answer[0] = liquid[num];	// answer�� 3���� ����� ������ sum�� ���� ��� 3���� ����
				answer[1] = liquid[left];
				answer[2] = liquid[right];
			}
			if (sum == 0) break;			// sum�� 0�̸� ���̻� Ž���� �ʿ䰡 ����
			if (sum > 0) right--;			// sum�� ũ�ٸ� ���� ���� �ʿ䰡 ����. right�� �ٿ���.
			if (sum < 0) left++;			// sum�� �۴ٸ� ���� Ű�� �ʿ䰡 ����. left�� �ٿ���.
		}
	}

	cout << answer[0] << " " << answer[1] << " " << answer[2];

	return 0;
}