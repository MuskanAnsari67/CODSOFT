def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take user input
    operation = input("Enter choice (1/2/3/4): ")

    # Take two numbers for calculation
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation based on operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator function
if __name__ == "__main__":
    calculate()