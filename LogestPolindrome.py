def isPalindrome(n):

   divisor = 1
   while (int(n / divisor) >= 10):
      divisor *= 10

   while (n != 0):
      leading = int(n / divisor)
      trailing = n % 10
  
      if (leading != trailing):
        return False

      n = int((n % divisor) / 10)

      divisor = int(divisor / 100)
   return True

# Function to find the largest palindromic element
def largestPalindrome(A, n) :
    # Sort the array
    A.sort()

    for i in range(n - 1, -1, -1) :
        # If number is palindrome
        if (isPalindrome(A[i])) :
            return A[i]    

    # If no palindromic number found
    return -1

# Driver Code 
arr = [1, 232, 5545455, 909090, 161]
n = len(arr) 
# print required answer 
print(largestPalindrome(arr, n))
Output
