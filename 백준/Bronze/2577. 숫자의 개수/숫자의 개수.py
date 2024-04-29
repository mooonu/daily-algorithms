result = 1
for _ in range(3):
    result *= int(input())

for i in range(10):
    print(str(result).count(str(i)))