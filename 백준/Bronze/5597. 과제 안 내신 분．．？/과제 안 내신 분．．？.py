N = []
student = set(range(1, 31))

for i in range(28):
    N.append(int(input()))

f_student = sorted(student.difference(N))
for i in f_student:
    print(i)