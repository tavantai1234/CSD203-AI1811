def binary_search_recursive(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, end)

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value1 = 5 
target_value2 = 11  

size_of_array = len(sorted_array)

result1 = binary_search_recursive(sorted_array, target_value1, 0, size_of_array - 1)
result2 = binary_search_recursive(sorted_array, target_value2, 0, size_of_array - 1)

print(f"Is {target_value1} present in the array? {result1}")
print(f"Is {target_value2} present in the array? {result2}")
