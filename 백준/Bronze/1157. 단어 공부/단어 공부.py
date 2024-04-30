l = input().lower()
s = list(set(l))
l2 = []

for i in s:
    l2.append(l.count(i))

if l2.count(max(l2)) > 1:
    print('?')
else:
    print(s[l2.index(max(l2))].upper())