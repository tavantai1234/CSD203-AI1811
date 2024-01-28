#1)
def puzzle(n):
    if n == 1: 
        return 1
    if n % 2 == 0:
        return puzzle(n/2)
    else:
        return puzzle(3*n+1)
for i in range(1,10):
    a = puzzle(i)
    print(a)

#2)
#2.1)
if n == 1:
    return 1

#2.2)
if n % 2 == 0:
    return puzzle(n/2)
else:
    return puzzle(3*n + 1)
#2.3) 
#\ invalid because the function just take one argument but the requirement is two argument

#3)
def show(n):
    if n>0:
        show(n/10)
    print(n%10)
n = show(123)
print(n)

#4)
def show(n):
    print(n%10)
    if n>0:
        show(n/10)
n = show(123)
print(n)

#5)
def show(n):
    print(n%10)
    if n>0:
        show(n/10)
    print(n%10)
n = show(145)
print(n)

#6)
def sum(n):
    if n == 1:
        return 1.0
    else:
        return 1/n + sum(n - 1)
n_value = 5 
result = sum(n_value)
print(f"The sum of {n_value} is: {result}")

#7)
