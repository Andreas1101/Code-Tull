import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def square(x):
    return math.sqrt(x)

print("Select operation: ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")
print("5. Square root ")
print("6. Prints value of pi ")
print("7. Prints value of e ")

while True:
    choice = input("Enter choice (1-7): ")

    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(number1,number2))

        elif choice == '2':
            print(sub(number1,number2))

        elif choice == '3':
            print(mul(number1,number2))

        elif choice == '4':
            print(div(number1,number2))

    elif choice in ('5'):
        number1 = float(input("Enter number to square: "))

        print(square(number1))

    elif choice in ('6'):
        print('Value of Pi is: ', math.pi)

    elif choice in ('7'):
        print('Value of e is: ', math.e)

    else:
        print("Invalid input!")
        break