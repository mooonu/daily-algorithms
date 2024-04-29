T = int(input())

for _ in range(T):
    ox = list(input())

    result = 0
    count = 0
    before = ''

    for j in ox:
        if j == 'O':
            if before == 'O':
                count += 1
                result += count
            else:
                count += 1
                result += 1
                before = j
        else:
            count = 0
    print(result)