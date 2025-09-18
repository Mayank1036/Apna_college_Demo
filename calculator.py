a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
c = input("Enter operator (+,-,*,/) = ")

if c == '+':
    print("Sum = ", a + b)
elif c == '-':
    print("Difference = ", a - b)
elif c == '*':
    print("multiplication =", a*b)
elif c == '/':
    if b != 0:  # division by zero
        print("ans = ", a / b)
    else:
        print(" Division by zero is not allowed")
else:
    print("You entered a wrong operator!")