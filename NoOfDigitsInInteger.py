def countDigit(n):
    digit = 0
    while n != 0:
        n //= 10
        digit += 1
    return digit
 
 
# Driver Code
n = 78673
print("Number of digits : % d" % (countDigit(n)))
