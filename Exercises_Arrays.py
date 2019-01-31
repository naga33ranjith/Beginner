#Exercises from Fundamentals of Computer programming with C sharp 
# Chapter Arrays

def Exercise1():
    for i in range(20):
        i=i*5
        ls.append(i)
    return ls
ls=[]
#Exercise1()
print("Elements in the list:",ls)


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
            for j in range(i):
                if(listforarray1[i]== listforarray2[j]):
                    return "Pass"

Exercise2()


        

