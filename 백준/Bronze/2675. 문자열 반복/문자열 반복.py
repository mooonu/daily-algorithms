for _ in range(int(input())):
    P = ''
    R, S = input().split()
    for i in S:
        P += i * int(R)
    print(P)