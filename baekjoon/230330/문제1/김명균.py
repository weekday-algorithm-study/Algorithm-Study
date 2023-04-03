"""
세 용액
문제: https://www.acmicpc.net/problem/2473
"""

import sys

input = sys.stdin.readline

n = int(input())

# 입력 받기
nums = list(map(int, input().split()))

# 투 포인터를 위한 정렬
nums.sort()

# 값 비교를 위한 초기화
find_value = sys.maxsize

# 정답 리스트
answer = []

# fix한 index를 위한 for문
for idx in range(n):
    # 투 포인터
    left = idx + 1
    right = n - 1
    while left < right:
        # 현재의 합
        tmp = nums[idx] + nums[left] + nums[right]
        # 찾는 값을 위한 비교
        if abs(tmp) < abs(find_value):
            find_value = tmp
            # 정답에 찾는 값들 넣기
            answer = [nums[idx], nums[left], nums[right]]

        # 만약 현재의 값이 0보다 작으면 왼쪽 포인터를 더 큰 값을 넣어준다.
        if tmp < 0:
            left += 1
        # 현재의 값이 0보다 크면 왼쪽 오른쪽 포인터에 더 작은 값을 넣어준다.
        elif tmp > 0:
            right -= 1
        # 0이면 출력 후 프로그램 종료
        else:
            print(*answer)
            sys.exit(0)

# 반복문이 끝나면 0에 가장 가까운 값이 answer 리스트에 담겨 있게 된다.
print(*answer)