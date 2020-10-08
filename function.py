num = int(input("enter num :"))


def factorial(x):
    if x == 1:
      
        return 1
    else:
        return (x * factorial(x-1))
print("factorial of number", num , "is", factorial(num))