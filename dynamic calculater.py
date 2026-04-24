print("Dynamic Calculator")

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Choose (+, -, *, /) or 'exit' to quit: ")

    if operation == "exit":
        print("Goodbye!")
        break

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")