my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key2'])

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'][0])
print(my_dict['key3'][0].upper())

print(my_dict)
my_dict['key1'] = my_dict['key1'] -123
print(my_dict)


my_dict1 = {}               # Returns Empty Dictionary
my_dict1['animal'] = 'Dog'
my_dict1['answer'] = 42
print(my_dict1)


print(my_dict1.keys())      # Returns List of keys
print(my_dict1.values())    # Returns List of Values
print(my_dict1.items())     # Returns tuples of each Item

print("############# Advanced Dictionaries ###################")

# iterating over Keys and Values
for k in my_dict1.keys():
    print(k)

for k in my_dict1.values():
    print(k)
# Dictionary Comprehensions Like List . But this is not Common
my_dict2 ={x:x**2 for x in range(10)}
print(my_dict2)


print("################# Tuples ##############################")
t = (1,2,3,3)
print(len(t))
print(t[0])
print(t[-1])


print(t.index(2))   # Prind the idex where value 3 is there
print(t.count(2))   # print the no of occirance of 2
print(t.count(3))   # print the no of occirance of 3

#t[0]= 'change' Will Give ERROR