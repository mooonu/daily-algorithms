def validation(n):
    return pow(int(n), 2)

num = list(map(validation, input().split()))
print(sum(num) % 10)
