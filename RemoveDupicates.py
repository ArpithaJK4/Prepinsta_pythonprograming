def remove_duplicates(arr, n):
    # Return if array is empty or contains a single element
    if n == 0 or n == 1:
        return n

    # Start traversing elements
    j = 0
    for i in range(0, n-1):
        # If current element is not equal to the next element, store the current element
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    # Store the last element as it is always unique in this context
    arr[j] = arr[n-1]
    j += 1

    return j

# Driver code
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
n = len(arr)

# Remove duplicates and get the new size of the array
n = remove_duplicates(arr, n)

# Print updated array
for i in range(n):
    print(arr[i], end=" ")

# Output: 10 20 30 40 50
