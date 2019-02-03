from math import *

def Exercise1():
    number=int(input("Enter an integer"))
    number1=int(input("Enter an integer"))
    if number>number1:
        number1=number
        print(number);print(number1)
    else:
        print(number);print(number1)

def Exercise2():
    ls=[]
    Number1=int(input("Enter Number1"))
    Number2=int(input("Enter Number2"))
    Number3=int(input("Enter Number3"))
    ls.append(Number1);ls.append(Number2);ls.append(Number3)
   
    
def Exercise3():

    Number1=int(input("Enter Number1"))
    Number2=int(input("Enter Number2"))
    Number3=int(input("Enter Number3"))
    if Number1>Number2 and Number1>Number3:

        print("Big of all numbers is :",Number1)
    elif Number2>Number1 and Number2>Number3:
        print("Big of all numbers is :",Number2)
    else:
        print("Big of all numbers is :",Number3)

def Exercise4():
    Number1=int(input("Enter Number1"))
    Number2=int(input("Enter Number2"))
    Number3=int(input("Enter Number3"))
    ls=[]
    ls.append(Number1);ls.append(Number2);ls.append(Number3)
    ls.sort()
    ls.reverse()
    print("After sorting elements in list",ls)
def Exercise5():
    Password_Book={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"       
        }
    Number=int(input("Enter an digit with in (0-9)"))
    print("Password is:",Password_Book[Number])

def Exercise5():

    Coefficient_of_X2=int(input("Enter number"))
    Coefficient_of_X=int(input("Enter number"))
    Constant=int(input("Enter Constant"))
    discrimiant=sqrt((Coefficient_of_X*Coefficient_of_X)-(4*Coefficient_of_X2*Constant))
    if discrimiant is 0:
        print("The quadratic equation is having rreal and equal roots")
        print("Roots are {0} {1} ",-Coefficient_of_X/2,-Coefficient_of_X/2)

    elif discrimiant>0:
        print("the quadratic equation having real and unequal roots")
        print("Roots are {0} {1}",(-Coefficient_of_X+discrimiant)/2,(-Coefficient_of_X-discrimiant)/2)
    else:
        print("Quadratic equation having imaginary roots")
    
def Exercise6():        