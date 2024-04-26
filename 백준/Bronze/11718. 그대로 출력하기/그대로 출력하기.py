import sys
# 빈줄은 주어지지 않는다. 만약 빈줄이 나온다면 반복을 종료할것
while True:
    a = sys.stdin.readline().strip()
    if a == "":
        break
    else:
        print(a)