"""for num in range(1,11):
    if num %2 == 0:
        print(num)"""


num = 5
sum = 1
for x in range(1,num +1):
    sum *= x
print(f"Loop: {sum}")


#Recursion is kind of like a loop
#Recursion operates through functions that call themselves.

def factorial(n):
    if n == 1: return 1#Base Case, the bottom of your recursion, when you want the function to stop calling itself.
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")

fib = [1,1]

for i in range(1,11):
    fib.append(fib[i-1] + fib[i])

print(f"Loop: {fib}")

numbers = []
def fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Recursion: {fibonacci(11)}")