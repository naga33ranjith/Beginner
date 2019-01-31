Number1=int(input("Enter first Number"))
Number2=int(input("Enter Second Number"))
print("Enter 1 for Adittion\n2for Subtraction\n3 for Multiplication\n4 for Division")
operator=int(input())
if operator==1:
    print("Addition Equals to ",Number1+Number2)
elif operator==2:
    print("Subtraction Equals to ",Number1-Number2)
elif operator==3:
    print("Multiplication equals to",Number1*Number2)
elif operator==4:
    print("Divison of two numbers",Number1/Number2)
else:
    print("Entered invalid operator")
