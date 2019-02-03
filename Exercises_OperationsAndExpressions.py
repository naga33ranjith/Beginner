def Exercise1():
    Number=int(input("Enter a Number"))
    if Number%2==0:
        print("Entered number is an integer")
    else:
        print("Entered number is not an integer")
def Exercise2():

    Is_integer=False

    Number= int(input("Enter a number"))
    if Number%5==0  and Number%7==0:
        Is_integer=True
        print(Is_integer)
    else:
        print(Is_integer)
def Exercise5():
    try:
        side_a=int(input("Enter the side"))
        side_b=int(input("Enter the side"))
        height=int(input("Enter the height"))
        print("Area of a trapeziod:",(side_a*side_b)/height)
    except ValueError as err:
        print(err)
def Exercise6():
    Side=int(input("Enter the Side of a rectangle"))
    height=int(input("Enter the height"))
    print("Area of the reactangle",Side*height)
    print("Perimeter of the rectangle",2*(Side+height))
def Exercise7():
    Weight=int(input("Enter weight"))
    print("Your Weight on earth",Weight)
    print("Your Weight on moon",0.17*Weight)
def Exercise8():
    Co_ordinate_X=float(input("Enter Number"))
    Co_ordinate_Y=float(input("Enter Number"))
    radius_of_Circle=5
    print(Check(Co_ordinate_X,Co_ordinate_Y,radius_of_Circle))
def Check(x,y,radius):
    
    if (x*x)+(y*y)<=(radius*radius):
        return True
    else:
        return False
def Exercise10():
    #Creating an empty list
    ls=[]
    Number=int(input("Enter an integer"))
    a=Number/10;b=(Number/10)%10;c=(Number/100)%10;d=(Number/1000)%10
    #Appending a,b,c and d elements to the list
    ls.append(a);ls.append(b);ls.append(c);ls.append(d)
    print(ls)
    print(ls.reverse())
    list2=ls.copy()
    print("Popped_element:",popped_element=list2.pop())
    
def Exercise11():
    Number=int(input("Enter an integer"))
    Position=int(input("Enter position"))



