def Prime_Factorial(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2, int(2+n//2)):
            if i == (1 + n // 2):
                arr.append(n)
                n = n // n
            if n % i == 0:
                arr.append(i)
                n = n // i
                break
    return arr


n = 210
print(Prime_Factorial(n))
