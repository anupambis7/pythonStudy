

print("################ Lambda expressions  #######################")
def square(x):
    return x*x
print("Normal Function : " + str(square(2)))

square = lambda x: x*x
print("Lambda Function : " + str(square(2)))


print("#################### FILTER ##########################")
# The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False).
# This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result.

def printLst(lst):
    for l in lst:
        print(str(l)+',' , end = ' ')
    print('\n')

def even_check(num):
    if num%2 ==0:
        return True

lst = [1,2,3,4,5,6,7,8,10]
flter1= filter (even_check , lst)
printLst(flter1)


filter2= filter(lambda x: x%2 ==0,lst)
printLst(filter2)

print("#################### MAP Function ##########################")

def fahrenheit(T):
    return ((float(9) / 5) * T + 32)

def celsius(T):
    return (float(5) / 9) * (T - 32)


temp = [0, 22.5, 40, 100]

tempF = map(fahrenheit,temp)
tempC = map(celsius,temp)

print ("Result of Map ")
printLst(tempF)
printLst(tempC)

tempFLam = map(lambda x:  (float(9)/5) *x +32, temp)
tempCLam = map(lambda x:  (float(5)/9) * (x -32), temp)

print ("Result of Map with lamda")
printLst(tempFLam)
printLst(tempCLam)

#map() can be applied to more than one iterable. The iterables have to have the same length.
#For instance, if we are working with two lists-map() will apply its lambda function to the elements of the argument lists,
# i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached.

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

res1= map(lambda x,y:x+y,a,b)
res2= map(lambda x,y,z:x+y+z, a,b,c)

print ("Result of Map with multiple Iterators")
printLst(res1)
printLst(res2)


print("#################### Reduce Function ##########################")

from functools import reduce
lstReduce =[47,11,42,13,100,1]

redRes1 = reduce(lambda x,y: x+y,lstReduce)

print ("Result of Reduce to find sum is :" + str(redRes1))

redRes2= reduce(lambda x,y: x if (x > y)  else y ,lstReduce)
print ("Result of Reduce to find Max is :" + str(redRes2))
