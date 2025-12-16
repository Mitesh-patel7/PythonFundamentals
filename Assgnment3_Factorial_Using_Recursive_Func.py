num = int(input("Enter the Number: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        facto = n * factorial(n - 1)
        return facto

print(f'Factorial of {num} is : {factorial(num)}')