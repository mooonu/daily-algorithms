alp = list(map(chr, range(97, 123)))

S = input()
for i in range(len(alp)):
    if alp[i] in S:
        print(S.index(alp[i]), end=" ")
    else:
        print(-1, end=" ")