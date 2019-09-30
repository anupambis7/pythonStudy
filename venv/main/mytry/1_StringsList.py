print("############# STRING ###################")
s= 'Hello World'
print(s)        # Prints out the Strings

# Escape sequence
s= "Hello'World"
print(s)
s= 'Hello\'World'
print(s)

print("String Intexing")
print(s[0])     # Printing the first element
print(s[1])     # Printing the second element
print(s[1:])    # Printing from second till end
print(s[:3])    #Printing the first 3 elements
print (s[:])    # Printing all the elements
print(s[-1])    # Printing the Last element
print (s[:-1])  # Print All but the last element

print("String Intexing to skip")
print(s[::1])
print(s[::2])
print(s[::-1])

print("Basic String functions")
print(s.upper())
print(s.lower())
print(s.split())
print(s.split('W'))

print("Formatting a String")
print('Insert another string with curly brackets {}'.format("The Inserted String"))
print('String 1: {} String 2 {}'.format("string1Arg","string2Arg"))

print('Here is a string: {} and this is the number {}'.format("STRING",5))
print('Here is a string: {} and this is the number {}'.format("STRING",5.4))

print('Here is a string: {a} and this is the number {b} using allias Eg 1'.format(a = "STRING",b = 5.4))                      # Using alias for format
print('Here is a string: {0} and this is the number {1} using allas Eg2'.format("STRING",5.4))                                # Using alias for format

print('Here is a string: {} and this is the number formatted is: {:2.2f}'.format("STRING",5.4))
print('Here is a string: {a} and this is the number formatted  {b:2.2f}'.format(a = "STRING",b = 5.4))      # using allias and putting the format
# for more formats refer https://pyformat.info/


print("############# LIST ###################")
print("Indexing and Slicing")
lst = [1,2,3,"Anupam"]
print(lst[0])
print(lst[-1])
print(lst[:2])
print(lst[2:])
print(lst[:])
print(lst[:-1])

print("Basic Methods in List")
print(lst + ["Tania"])      # This adds "Tania" in a new list. Doesnot append to the ogiginal list
print(lst.append("Happy"))  # This adds "Happy" to the ogiginal list

print("List before Pop(0) is : " + str(lst))
print(lst.pop(0))
print("List After Pop(0) is : " + str(lst))
print(lst.pop())
print("List After Pop()[By default takes pop(-1) ] is : " + str(lst))

lst = [1,2,3,4,5,6,7,8,9]
print(lst[:: 2])
print(lst[:: -1])
print(lst)
lst.reverse()
print("Print list after Reverse is :" + str(lst))
lst.sort()
print("Print list after Sort is :" + str(lst))

print("Other Advanced List Functions")
print(lst)
lst.remove(4)
print("List after removing 4" + str(lst))
lst.insert(3,'4-Inserted')
print("List after Inserting" + str(lst))
lst.extend([10,11])         # This extends by putting elemenst from iterable
print(lst)
lst.append([10,11])         # Append aoject at the end . So it appends [10,11] as a List
print(lst)
print("Index of 3 is :" + str(lst.index(3)))

lst1 = ["A","B"]
lst2 = lst1
lst3 = lst1[:]
lst1.append("C")
print("List 1 contents is :" + str(lst1))
print("List 2 contents is :" + str(lst2))
print("List 3 contents is :" + str(lst3))


print("############# List Comprehensions ###################")

lst = [x for x in 'word']
print(lst)
lst = [x**2 for x in range(0,11)]
print(lst)
lst = [x for x in range(0,11) if x %2 ==0]
print(lst)
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5 )*temp +32) for temp in celsius]
print(fahrenheit)