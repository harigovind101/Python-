num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
operator = input("enter the operator:")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("invalid operator")

print(num1,operator,num2,"=",result)
