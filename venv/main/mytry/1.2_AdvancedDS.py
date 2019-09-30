# Ref https://www.youtube.com/watch?v=l_5bPOV7qB8&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf&index=35

####################### SET #############################

colour = {'red','black','yellow','green','red'}
print(colour) # Notice it doenot allow duplicates

# Creating an empty set
colour = set() # we cannot use {} as its used to create an empty dictionary
print(colour)
colour.add('red')
print(colour)

# Checking if set has a perticular element
print("Checking if set has a particular element")
print( 'red' in colour)
print( 'black' in colour)

# Convert List to Set
print(set([1,2,3,4,4])) # We can see as it converts to set the duplicate element is removed

## Some Set Operations

set1 = set([1,2,4,5,9,0])
set2 = set([1,2,6,7])
print("***** UNION *****")
print(set1 | set2)
print("***** INTERSECTION *****")
print(set1 & set2)
print("***** SET DIFFERENCE *****")
print(set1 - set2)
print("***** EXCLUSIVE OR *****")
print(set1 ^ set2)


####################### STACKS AND QUEUE #############################
# We we impose some descpline in the way we can pull and put records in a List we get Stacks and Queues
# Now Stack is Last in first out
# Queue is First In first out. as a generic queue the person who can first gets priority

# stack is implemented by the following functins
# push (s,x) -- add x to stack s
# pop (s) - returns the recently added elements ,
# we can achive the same using python list using these functions
print ("#####  STACKS Usecase ####")
list1 = [1,2,3]
list1.append(4)
print(list1)
print(list1.pop())
print(list1)

# Queue is implemented by the following functins
# addq (q,x) -- add x to queue q
# removeq (q) - removes the element head of queue
# we can achive the same using python list using these functions

print ("#####  Queue Usecase ####")
list1 = [1,2,3]
list1.insert(0,4)
print(list1)
print(list1.pop())
print(list1)