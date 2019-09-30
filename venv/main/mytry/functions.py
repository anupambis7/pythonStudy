def convert_to_celcious(fahrenheit) :
    """
    (number) ->float
    """
    temp = fahrenheit -32
    #(temp) * 5 / 9  [Note : If we remove the return keyword it returns None]
    return (temp) *5/9


result1= convert_to_celcious(80)


print(result1)
# if else statement

def ifElseFn (num):
    if num > 100:
       print("Greater than 100")
    elif num < 100 and num >50:
        print("Number between 100 and 50")
    else :
        print("Others")

ifElseFn(99)

def ifElseFn2 (num):
    if num > 100:
       result ="Greater than 100"
    elif num < 100 and num >50:
        result ="Number between 100 and 50"
    else :
        result ="Others"
    return result

print(ifElseFn2(99))

# Using methods
print(str.capitalize('bowwowing'))

name1 = str('borrowing')
print(name1.capitalize())
print('borrowing'.capitalize()) # calling methods object oriented way


lst =[1,2,3]

def addition(n):
    return n + n
lst2 = map(addition,lst)

for i in lst2:
    print(i)