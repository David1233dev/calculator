number1 = int(input("First Number:"))
action = input("Action:")
number2 = int(input("Second Numbrt:"))

if action == "+":
    results = number1 + number2
    print(results)
elif action == "-":
    results = number1 - number2
    print(results)
elif action == "*":
    results = number1 * number2
    print(results)
else:
    print("Invalid")
    
