first = int(input("enter your first number :"))
operator = input("enter your operator (+,-,*,/,%)")
second = int(input("enter your second number "))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else :
    print("invalid opration")
    print("pleas select above oprator")
    print("pleas check your numbers and the oprator")
