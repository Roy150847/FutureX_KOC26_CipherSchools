# PROGRAM TO CHECK IF A NUMBER IS IN FIBONACCI SERIES OR NOT

# defining a function to check if the given number is in fibonacci series or not 

def fibonacci(num):
    a = 0
    b = 1
    if num == 0 or num == 1 :
        return 1
    while b <= num :
        c = a + b
        a = b
        b = c
        if c == num:
            return 1
            break

# taking input from the user

x = 1
while x == 1:
    number = int(input("Enter the number: "))

    # Calling the function to check if the given number is in fibonacci series or not

    if fibonacci(number) == 1 :
        print("The given number is in Fibonacci Series")
    else :
        print("The given number is not in Fibonacci series")

    # Checking if the user wants to check for more number

    x = int(input("Enter 1 if you want to check for more number: "))

print("Thank You")

