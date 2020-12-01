print('#'*10)
print('Multiple *Arguments and **Key Word Arguments')
print('*args and **kwargs')
print('its the stars * and ** that matter, *params, **example')
print('for convention use args and kwargs names')
print('#'*10)
def myFunc(a,b):
    #Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myFunc(40,60))
print()
print('*args allows your to pass in as many arguments as possible and treats it like a tuple')

def myBetterFunc(*args):
    return sum(args) * 0.05

print(myBetterFunc(10,20,20,25,25))
print()
print('** generates a key word dictionary of arguments')
def myCoolFunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    elif 'fish' in kwargs:
        print('{} is a type of fish'.format(kwargs['fish']))
    else:
        print('I did not find any fruit here')

myCoolFunc(fruit='apple', veggie='lettuce', fish='king klip')
myCoolFunc(veggie='lettuce', fish='King klip')

def myBestestFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

myBestestFunc(10,20,30, fruit='orange', food='eggs', animal='dog')
print()
print('* and ** can be used together')

def mySunk(*args):
    mylist = []
    for arg in args:
        if arg % 2 == 0:
            mylist.append(arg)
    return mylist

print(mySunk(2,3,4,5,6))

def myStringFun(myString):
    newString = ''
    count = 1
    for letter in myString:
        if  count % 2 == 0:
            newString += letter.upper()
            count += 1
        else:
            newString += letter.lower()
            count += 1
    return newString

print(myStringFun('Steve'))