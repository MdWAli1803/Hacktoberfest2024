def find_min(arr):
    if not arr:
        return None  # Return None if the array is empty
    
    min_element = arr[0]  # Assume the first element is the min
    for num in arr:
        if num < min_element:
            min_element = num  # Update min_element if a smaller number is found
            
    return min_element

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value = find_min(array)
print(f"The minimum element in the array is: {min_value}")
