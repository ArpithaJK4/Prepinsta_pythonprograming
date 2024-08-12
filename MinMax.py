a =[10,89,9,56,4,80,8]
min=a[0]
max=a[0]


for i in range(len(a)):
    if a[i] < min:
       min=a[i]
    if a[i] >max:
        max=a[i]
print(min)
print(max)



