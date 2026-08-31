# Valid Palindrome — 핵심

**함정**: 필터링해놓고 정작 비교는 원본 `s`로 하면 안 된다. 걸러낸 `filtered_s`끼리 비교해야 한다.

- 문자 판별: 영숫자만 → `c.isalnum()` (숫자도 포함해야 함. `"0P"`는 팰린드롬 아님)
- 정규화: `c.lower()` (대소문자 무시)

## 이 풀이 (필터 + 양끝 비교)
```python
filtered_s = [c.lower() for c in s if c.isalnum()]
for i in range(len(filtered_s) // 2):
    if filtered_s[i] != filtered_s[-i - 1]:
        return False
return True
```
시간 O(n) · 공간 O(n)

## O(1) 공간 — 투 포인터 (면접 기대 답)
새 리스트를 안 만들고 양끝에서 좁힌다.
```python
i, j = 0, len(s) - 1
while i < j:
    while i < j and not s[i].isalnum(): i += 1
    while i < j and not s[j].isalnum(): j -= 1
    if s[i].lower() != s[j].lower():
        return False
    i += 1; j -= 1
return True
```
시간 O(n) · 공간 **O(1)**

## 2022년 풀이 (regex 한 줄)
```python
org = re.sub(r'[^a-z0-9]+', '', s.lower())
return org == org[::-1]
```
