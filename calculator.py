def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "You can't divide by zero!"
    return x / y

# Operation selection
print("Select operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter the number of the operation (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    except ValueError:
        print("Please enter valid numbers!")
else:
    print("Invalid operation choice.")