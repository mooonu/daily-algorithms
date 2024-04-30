l = input().lower()
s = set(l)
l2 = []

# 중복 제거한 리스트의 원소로 중복을 제거하지 않은 리스트를 탐색함
for i in s:
    l2.append(l.count(i))

max_value = max(l2)
s = list(s)

# max() 의 값이 1개 이상이라면 ? count 로 확인
if l2.count(max_value) > 1:
    print('?')
else:
    # 어떤 알파벳이 많았는지 대문자로 출력해야함
    print(s[l2.index(max_value)].upper())

# max_value 의 인덱스 값을 찾고 리스트로 변환한 s[찾은 인덱스 값]