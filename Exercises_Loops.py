from math import factorial
from array import *
import random


def Exercise1():
    Number=int(input("Enter Number"))
    for i in range(Number):
        print(i)
def Exercise2():
    li=[]
    Number=int(input("Enter Number"))
    for i in range(Number):
        if not(i%3==0 and i%7==0):
            li.append(i)
        
    print(li)
def Exercise3():
    number=int(input("Enter number"))
    ls=[]
    for i in range(number):
        x=int(input("Enter number"))
        ls.append(x)

    
    print("Maximum number is:",max(ls))
    print("Minimunm number is :",min(ls))
def Exercise4():

    number=int(input("Enter number"))
    firstnumber=0;secondnumber=1
    ls=[]
    ls.append(firstnumber);ls.append(secondnumber)
    for i in range(2,number):
        x=ls[i-1]+ls[i-2]
        ls.append(x)
    print(ls)
def Exercise5():
    Value_N=int(input("Enter number"))
    Value_k=int(input("Enter number"))
    if Value_N>Value_k and Value_k>1:
        print("value is:",factorial(Value_N)/factorial(Value_k)) 

    else:
        print("invalid values")
def Exercise6():
    n=int(input("Enter number"))
    if n>=0:

        Numerator=factorial(2*n)
        Denominator=factorial(n+1)*factorial(n)
        
        Catalan_numbers=Numerator/Denominator
        print("Output",Catalan_numbers)
    else:
        print("Enter valid input")
def Exercise7():

    Value_N=int(input("Enter number"))
    Value_k=int(input("Enter number"))
    if Value_N>Value_k and Value_k>1:
        Numerator=factorial(Value_N)*factorial(Value_k)
        Denominator=factorial(Value_N-Value_k)
        print("result",Numerator/Denominator)
    else:
        print("invalid input")
def Exercise8():
    n=int(input("Enter number"))
    x=int(input("Enter number"))
    result=0
    for i in range(n):
        result=factorial(i)/pow(x,i)
        result+=result
    print("Result",result+1)
def Exercise9():
    number=int(input("Enter number"))
    count=0
    result=factorial(number)
    x = str(result)
    xRev  = x[::-1]
    count = 0
    for i in xRev:
        if i == '0':
            count = count + 1
        else :
            break
    print(count) 
def generator(inputValue):


    startValue = 1
    endValue = inputValue
    for i in range(1, inputValue+1):
        line = []
        for j in range(startValue, endValue+1):
            line.append(j)
        print(line)
        print("\n")
        startValue = startValue + 1;
        endValue = endValue + 1
def Exercise12():
    number=int(input("Enter Number"))
    print("Binary notation of the given  number is:",bin(number))
def Exercise13():
    number=int(input("Enter Number"))
    print("Decimal format of the number",int(number,2))
def Exercise14():
    number=int(input("Enter number"))
    print("Number is ",hex(number))
def Exercise15():
    number=int(input("Enter number "))
    print("decimal format of entere number is",int(number,16))
def Exercise16():
    number=int(input("Entered number"))
    print(random.randrange(1,number))
   
def Exercise17():
    number1=int(input("Enter number"))
    number2=int(input("Enter mumber"))
    set1={};set2={}
    #finding Greatest common divisor og given two integers'
    for i in range(number1):
        if number1%i == 0:
            set1.update(i)
    for j in range(number2):
        if number2%i==0:
            set2.update(j)
    
    set3=set.intersection(set1,set2)
    a=max(list(set3))
    print("Greatest common divisor",a)
    #to find Lease common multiple
    lcm=abs(number1*number2)/(a)
    print("lcm is",lcm)
    
