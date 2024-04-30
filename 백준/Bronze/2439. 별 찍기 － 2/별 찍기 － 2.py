T = int(input())
k = 0
for i in range(T, 0, -1):
    k += 1
    for j in range(i-1):
        print(end=" ")
    print('*' * k)