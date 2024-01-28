def find_sum_recursive(arr, n):
    if n == 1:
        return arr[0]
    else:
        return arr[0] + find_sum_recursive(arr[1:], n - 1)

array_example = [5, 2, 8, 1, 3]  
size_of_array = len(array_example)
result = find_sum_recursive(array_example, size_of_array)
print(f"The sum of all elements in the array is: {result}")
