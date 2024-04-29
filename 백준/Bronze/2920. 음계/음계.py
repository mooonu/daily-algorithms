l = list(map(int, input().split()))

if l[0] == 1:
    s = sorted(l)
else:
    s = sorted(l, reverse=True)

if l == s:
    if l[0] == 1:
        print('ascending')
    else:
        print('descending')
else:
    print('mixed')