def count_distinct_elements(arr):
    # Initialize an empty dictionary to keep track of element frequencies
    element_count = {}

    # Iterate over each element in the array
    for element in arr:
        # If the element is not in the dictionary, add it with a count of 1
        if element not in element_count:
            element_count[element] = 1

    # The number of keys in the dictionary represents the number of distinct elements
    return len(element_count)

# Example usage:
array = [7, 8, 9, 7, 6, 6, 10]
distinct_count = count_distinct_elements(array)
print(f"The number of distinct elements is: {distinct_count}")
