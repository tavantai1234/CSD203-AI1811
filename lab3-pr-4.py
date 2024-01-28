def is_palindrome_recursive(arr, n):
    if n <= 1:
        return 1
    else:
        return (arr[0] == arr[n-1]) and is_palindrome_recursive(arr[1:n-1], n-2)

array_example1 = [1, 2, 3, 2, 1]  
array_example2 = [1, 2, 3, 4, 5]  

size_of_array1 = len(array_example1)
size_of_array2 = len(array_example2)

result1 = is_palindrome_recursive(array_example1, size_of_array1)
result2 = is_palindrome_recursive(array_example2, size_of_array2)

print(f"Is array_example1 a palindrome? {result1}")
print(f"Is array_example2 a palindrome? {result2}")
