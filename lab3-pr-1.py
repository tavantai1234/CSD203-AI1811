def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

n_value = 5  
result = recursive_sum(n_value)
print(f"The sum of numbers from 1 to {n_value} is: {result}")
