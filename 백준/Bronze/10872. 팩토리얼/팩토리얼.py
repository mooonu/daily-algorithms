a = int(input())

def test(n):
    if n > 1:
        return n * test(n - 1)
    else:
        return 1

print(test(a))