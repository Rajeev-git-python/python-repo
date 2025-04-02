
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        # recursive call to the function
        return (num * factorial(num - 1))



num= int(input("Enter a number :"))

res= factorial(num)
print(f'Factorial of {num} is:', res)

