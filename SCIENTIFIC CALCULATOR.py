import math
a=input("TO START OR CONTINUE ENTER Y:  ")
while a=='Y':
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'pow' for exponentiation")
    print("Enter 'sqrt' for square root")
    print("Enter 'sin' for sine")
    print("Enter 'cos' for cosine")
    print("Enter 'tan' for tangent")
    print("Enter 'asin' for arcsine (sin^-1)")
    print("Enter 'acos' for arccosine (cos^-1)")
    print("Enter 'atan' for arctangent (tan^-1)")
    print("Enter 'c2f' for Celsius to Fahrenheit")
    print("Enter 'c2k' for Celsius to Kelvin")
    print("Enter 'f2c' for Fahrenheit to Celsius")
    print("Enter 'f2k' for Fahrenheit to Kelvin")
    print("Enter 'k2c' for Kelvin to Celsius")
    print("Enter 'k2f' for Kelvin to Fahrenheit")
    print("Enter 'quit' to end the program")
    
    user_input = input("Enter: ")

    if user_input == "quit":
        break
    elif user_input in ("add", "sub", "mul", "div", "pow", "sqrt", "sin", "cos", "tan", "asin", "acos", "atan"):
        num1 = float(input("Enter first number: "))
        
        if user_input not in ("sqrt", "sin", "cos", "tan", "asin", "acos", "atan"):
            num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            result = num1 + num2
            
        elif user_input == "sub":
            result = num1 - num2
            
        elif user_input == "mul":
            result = num1 * num2
            
        elif user_input == "div":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
                
        elif user_input == "pow":
            result = num1 ** num2
            
        elif user_input == "sqrt":
            result = math.sqrt(num1)
            
        elif user_input == "sin":
            result = math.sin(num1)
            
        elif user_input == "cos":
            result = math.cos(num1)
            
        elif user_input == "tan":
            result = math.tan(num1)
            
        elif user_input == "asin":
            result = math.asin(num1)
            
        elif user_input == "acos":
            result = math.acos(num1)
            
        elif user_input == "atan":
            result = math.atan(num1)
            
    elif user_input in ("c2f", "c2k"):
        temp_celsius = float(input("Enter temperature in Celsius: "))
        
        if user_input == "c2f":
            result = (temp_celsius * 9/5) + 32
            
        elif user_input == "c2k":
            result = temp_celsius + 273.15
            
    elif user_input in ("f2c", "f2k"):
        temp_celsius = float(input("Enter temperature in Fahrenheit: "))
        
        if user_input == "f2c":
            result = (temp_celsius - 32) * 5/9
            
        elif user_input == "f2k":
            result = (temp_celsius - 32) * 5/9 + 273.15

    elif user_input in ("k2f", "k2c"):
        temp_celsius = float(input("Enter temperature in Kelvin: "))
        
        if user_input == "k2c":
            result = temp_celsius - 273.15
            
        elif user_input == "k2f":
            result = (temp_celsius - 273.15) * 9/5 + 32
    else:
        print("Invalid input. Please enter a valid option.")
        continue
    print(f"Result: {result}")
    a=input("TO START OR CONTINUE ENTER Y:  ")