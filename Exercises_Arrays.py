#Exercises from Fundamentals of Computer programming with C sharp 
# Chapter Arrays

import array as arr

import random as r    
def Exercise1():
    ls=[]
    for i in range(20):
        i=i*5
        ls.append(i)
    print(ls)


def Exercise2():
    array1=int(input("Enter the size of the first array:"))
    array2=int(input("Enter the size of the second array:"))
    listforarray1=[]
    listforarray2=[]
    for i in range(array1):
        a = int(input("Enter the number in array1"))
        listforarray1.append(a)
    for i in range(array2):
        a = int(input("Enter the number in a"))
        listforarray2.append(a)
    if len(listforarray1) == len(listforarray2):
        for i in enumerate(listforarray1):
            if(listforarray1[i]== listforarray2[i]):
                print("Equal")
            else:
                print("not equal")                    
    else:
        print("Length of lists are not equal")

ls=[]


def Exercise4():
    li=[1,1,2,3,2,2,2,1]
    countofelements=[]
    for i in range(len(li)):
        for j in i:
            li.count(li[i])
            countofelements.append(li[i])

def Exercise5():
    li=[3,2,3,4,2,2,4]
    answer=[]
    for i in range(len(li)-1):
        if(li[i]<li[i+1]):
            answer.append(li[i])
    print(answer)

Exercise5() 