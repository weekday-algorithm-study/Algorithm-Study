## 접근 방식
문자열은 sort가 아니라 sorted를 해야하고 이 경우 리스트로 반환됩니다.
시간복잡도는 O(m*nlogn)입니다.
m => for문, nlogn => sorted
## 문제 풀이
```python
def groupAnagrams(self, strs):
	strs_table = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))

        if sorted_string not in strs_table:
            strs_table[sorted_string] = []

        strs_table[sorted_string].append(string)

    return list(strs_table.values())
```