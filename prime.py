def Prime_Number(n):
    for i in range(2,1+n//2):
        if n % i == 0:
            return False
    return True


n = 979
if Prime_Number(n):
    print("Yes,", n, "is Prime")
else:
    print("No,", n, "is not a Prime")
