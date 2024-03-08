op = input("Enter operator: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Sorry type again")
