def checker(s):
    if s.islower():
        return s.upper()
    else:
        return s.lower()


s = list(map(checker, input()))
for i in s:
    print(i, end="")