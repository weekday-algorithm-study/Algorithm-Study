#include <iostream>
#include <vector>
#include <algorithm> // sort 함수

using namespace std;

int N; // N의 최대치는 5000이므로 int로 선언.
long long small = 3000000000 + 1; // 용액의 특성값 최대치 1,000,000,000가 3번 중복될 수 있으므로 최대치인 3,000,000,000 + 1로 초기화
vector<long long> answer(3); // 최소값을 만드는 용액의 특성 3개를 저장할 vector 변수. 특성값 최대치는 1,000,000,000이므로 long long으로 선언.

int main(void)
{
	cin >> N;

	vector<long long> liquid(N); // 주어지는 용액의 특성값을 저장할 vector 변수. 특성값이므로 long long
	for (int i = 0; i < N; i++) // N까지 반복할 i는 int로 선언해도 괜찮음
	{
		cin >> liquid[i];
	}
	sort(liquid.begin(), liquid.end()); // 받아온 용액의 특성값을 오름차순으로 정렬

	// ---------------------------------------------------------------------------------------
	// 
	// 오름차순으로 정렬된 용액의 배열에서 가장 작은 i를 첫번째 num으로 지정
	// num은 고정시킨 상태로 left와 right 두개의 포인터를 움직여 최소값을 탐색할것임
	// 
	// ---------------------------------------------------------------------------------------

	for (int i = 0; i < N; i++) {
		int num = i; // left와 right를 조정하는 동안 고정된 값을 가지고 있을 num
		int left = i; // 항상 배열의 가장 왼쪽 값을 배열을 left 포인터로 초기화
		int right = N - 1; // 항상 배열의 가장 오른쪽 값을 right 포인터로 초기화

		while (left != right)
		{
			if (left == i) { left++; continue; } // 만약 left가 num과 같은 상태라면 아래 과정을 스킵하고 다음으로 넘김
			if (right == i) { right--; continue; } // 만약 right가 num과 같은 상태라면 아래 과정을 스킵하고 다음으로 넘김

			long long sum = liquid[left] + liquid[right] + liquid[num]; // 세 용액의 합

			if (abs(sum) < small) // 음수가 존재하며, 0에 가장 가까운 값을 찾고 있으므로 절대값(abs)으로 비교해야함
			{								// 만약 sum의 절대값이 지금 가지고 있는 최소값보다 더 작다면
				small = abs(sum);			// 지금 가지고 있는 최소값을 sum의 절대값으로 변경
				answer[0] = liquid[num];	// answer의 3가지 용액을 현재의 sum을 만든 용액 3개로 변경
				answer[1] = liquid[left];
				answer[2] = liquid[right];
			}
			if (sum == 0) break;			// sum이 0이면 더이상 탐색할 필요가 없음
			if (sum > 0) right--;			// sum이 크다면 값을 줄일 필요가 있음. right를 줄여줌.
			if (sum < 0) left++;			// sum이 작다면 값을 키울 필요가 있음. left를 줄여줌.
		}
	}

	cout << answer[0] << " " << answer[1] << " " << answer[2];

	return 0;
}