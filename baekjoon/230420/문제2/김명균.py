"""
단어 뒤집기 2
문제: https://www.acmicpc.net/problem/17413
"""

# 단어 입력
s = input()

# 태그가 없는 경우
if "<" not in s:
    # 공백 기준으로 자르고
    s = s.split()

    for char in s:
        print(char[::-1], end=" ")
else:
    flag = True
    for i in range(len(s)):
        if s[i] == "<":
            flag = False