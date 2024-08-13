a = [10, 20, 5, 3, 40, 2, 11]
n = len(a)
for i in range(0, n):
for j in range(i + 1, n):

if a[i] > a[j]:
temp = a[i]
a[i] = a[j]
a[j] = temp

print(a)
