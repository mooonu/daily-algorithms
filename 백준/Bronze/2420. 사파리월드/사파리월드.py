n, m = map(int, input().split())
diff = n - m
if diff < 0:
    diff = -diff
print(diff)