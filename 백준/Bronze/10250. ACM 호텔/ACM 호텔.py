import math

for _ in range(int(input())):
    N_H = 0
    N_W = 0
    H, W, N = map(int, input().split())

    # N <= H 경우
    if N < H:
        N_H = str(math.trunc(N % H))
        N_W = '01'
        print(N_H + N_W)
    else:
        # N >= H 경우
        # 나머지가 0인 경우
        if N % H == 0:
            N_H = str(H)
            N_W = str(math.trunc(N / H))
        # 나머지가 0이 아닌 경우
        else:
            N_H = str(math.trunc(N % H))
            N_W = str(math.trunc(N / H) + 1)
        if int(N_W) < 10:
            N_W = '0' + str(N_W)
        print(N_H + N_W)