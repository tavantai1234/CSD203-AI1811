def find_min_recursive(arr, n):
    if n == 1:
        return arr[0]
    else:
        min_of_rest = find_min_recursive(arr[1:], n - 1)
        return min(arr[0], min_of_rest)

array_example = [5, 2, 8, 1, 3] 
size_of_array = len(array_example)
result = find_min_recursive(array_example, size_of_array)
print(f"The minimum element in the array is: {result}")
