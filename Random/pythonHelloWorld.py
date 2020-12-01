import sys
print ('hello world')
# comment is a hashtag
print()
print('####'*10)
print('Numbers in python')
print('####'*10)
print('Modulo Mod operator allows you to find out what is an even number')
print(50 % 5)
print(50 % 3)
print()
print('To the power of uses 2 stars like so 2 ** 4')
print(2 ** 4)
print(1/2)
print()
print('####'*10)
print('Variable Assignments in Python')
print('####'*10)
my_dogs = 3
print(type(my_dogs))
my_dogs = ["River","Amber", "Nala"]
print('python has dynamic typing for variables')
print('be aware of type() function to check type of any variable')
dataType = type(my_dogs)
print(dataType)
myname = "Steve Velcev"
sentence = "String are sequenced in Python, thus it has index values for each letter in the string."
print(sentence)
print("Use '\\n' to print a new line")
print('\n')
myNameLength = len(myname)
print('The lenght of my name including a space is')
print(myNameLength)
print(myname[-1])
print('\n')
print(myname[6:])
print(myname[:5])
print(myname[2:5])
print(myname[::2])
print("This will reverse a string")
print(myname[::-1])
letter = 'z'
print(letter*10)
print(letter.upper())
#format() method
print('My name is {}'.format('Steve'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
formatting = 'Insert another string with curly brackets: {}. {}'.format('The inserted string', "Does this work?")
print(formatting)
#float formatting follows "{value:width.precision f}"
print('The result was {r:1.3f}'.format(r = 100/777))
#f-string method introduced with python 3.6
name = 'Jose'
print('Remember the f infront of the string literal')
print(f'Hello my instructors name is {name}')
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
print()
print('####'*10)
print('Lists')
print('####'*10)
#lits in python are ordered, contain arbitary objects (can mix data and object types), can access via index, mutable
myList = [1,2,3]
myMixedList = ['String', 100, 123.45]
anotherList = myList + myMixedList
print(anotherList)
print('Lists are mutable')
anotherList[3] = 'Four'
anotherList.append('Six')
print(anotherList)
print('Popped item of list is removed from the list ' + anotherList.pop())
print(anotherList)
letterList = ['a', 'x', 'b', 'z']
numberList = [4,5,1,3,2,6]
letterList.sort()
print(letterList)
print()
print('####'*10)
print('Dictionaries')
print('####'*10)
myDictionary = {'Key':'Value', 'Name':'Steve', 'Age':29, 'Sex':'Male'}
print('My name is {}'.format(myDictionary['Name']))
print('My age is {}'.format(myDictionary['Age']))
capName = myDictionary['Name'].upper()
print(capName)
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())
spanish = dict()
spanish['hello'] = 'hola'
spanish['yes'] = 'si'
print(spanish['hello'])
print(spanish.values())
a = dict( one = 1, two = 2, three = 3)
print(a.values())
def createDictionary():
    '''Return a tiny spanish dictionary'''
    spanishNumbers = dict()
    spanishNumbers['one'] = 'uno'
    spanishNumbers['two'] = 'dos'
    spanishNumbers['three'] = 'tres'
    return spanishNumbers

someDictionary = createDictionary()
print('{} {} {}'.format(someDictionary['one'], someDictionary['two'], someDictionary['three']) )
#f you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object 
print()
print('####'*10)
print('Tuples')
print('####'*10)
print("In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.")
print('Instead of [] brackets we use () for tuples along with the commans in it')
myTuples = (4,3,1989)
print(type(myTuples))
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print('Why use Tuples?')
print('If in your program you are passing around an object and need to make sure it does not get changed, then a tuple becomes your solution. It provides a convenient source of data integrity.')
#this is how you delete a tuple
tup1 = (1,2,3)
del tup1
print()
print('####'*10)
print('Sets')
print('####'*10)
#Sets are an unordered collection of unique elements. We can construct them by using the set() function.
#sets have to have unique values.
myset = set()
myset.add(1)
myset.add(2)
mylist = [1,1,1,2,2,3,3,3,3]
print(myset)
print('When yo put a list into a set it will just take all the unique values')
print(mylist)
print(set(mylist))
print()
print('####'*10)
print('Global Variables')
print('####'*10)
def randomPrint():
    variable = 'I love South Africa' # local variable
    print(variable)
#cant use global and local variables 
variable = 'I love America' #global variable
randomPrint()
print(variable)
print()
print('####'*10)
print('Loops')
print('####'*10)
animals = ['cat', 'dog', 'fish', 'python']
# for loop with a list
for animal in animals:
    print(animal, len(animal))

for count in (1,2,3,4,5):
    print('down')
    print(count)
    print("yes" * count)

for colour in ('red', 'green', 'blue'):
    print(colour)
#while loops repeats as long as a certain bolean condition is met
number = 0
while number < 11:
    print(number)
    number += 1

myNumberList = [1,2,3,4,5,6,7,8,9,10]
for num in myNumberList:
    if num % 2 == 0:
        print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')

print()
print('Tuple Unpacking')
myTupleList = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myTupleList:
    print(b)
#this will print the middle value in the tuple
#same thing can be done with a dictionary 

# break can be used to exit a for or while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break #breaks out of the while loop here when the if condition is met.

loopKeywords ='''
break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.
'''
print(loopKeywords)
#conditional execution
print()
print('####'*10)
print('Conditional execution')
print('####'*10)
print(5 == 5)
print(5 != 6)
# <> != == > <
x = 10
somethingTrue = (x == 10)
print(somethingTrue) 
y = 100
somethingFalse = (y != 100)
print(somethingFalse)
print()
print('####'*10)
print('if statements')
print('####'*10)

zero = 0
if zero == 0:
    print('zero is 0')

x = 6
if x%2 == 0:
    print('x is even')
else:
    print('x is odd')

z = 6
y = 5
if z == y:
    print('z and y are equal')
else:
    if z < y:
        print('z is less than  y')
    else:
        print('z is greater than y')

weight = float(input('How many kilograms does your suitcase weigh? '))
if weight > 20:
    print('There is an extra charge for suitcases that weigh over 20KG')
else:
    print('Your suitcase is below the weight limit of 20KG')

#some additional if statement stuff like elif
print()
name = input('What is your name? ')
if name == 'Steve':
    print(f'Nice name {name}')
elif name == 'John':
    print(f'What a generic name {name} Doe')
else:
    print(f'Your name is ok {name}')

print()
print('####'*10)
print('Useful Operations')
print('####'*10)
print('range(start,stop,step)')
print('Note that this is a generator function, so to actually get a list out of it, we need to cast it to a list with list(). What is a generator? Its a special type of function that will generate information and not need to save it to memory.')
print(list(range(0,11)))
print()
print('enumerate')
print("Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this index_count or loop_count variable")
for i in enumerate('abcde'):
    print(i)
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
print()
print('zip')
print("You can use the zip() function to quickly create a list of tuples by 'zipping' up together two lists.")
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
print()
print('in')
print("We've already seen the in keyword during the for loop, but we can also use it to quickly check if an object is in a list")
if 'x' in ['x','y','z']:
    print('x is in our list')
print()
print('min and max')
print('Quickly check the minimum or maximum of a list with these functions.')
mylist = [10,20,30,40,100]
print('Min of my list is {}'.format(min(mylist)))
print('Max of my list is {}'.format(max(mylist)))
print()

print('random library')
from random import shuffle
print('shuffle(aList)')
from random import randint
print('randint(0,100) will return a random interger')
print(str(randint(0,100)))

print()
print('####'*10)
print('List Comprehensions')
print('####'*10)
myTestString = 'hello'
mmyTestList = []
for letter in myTestString:
    mmyTestList.append(letter)
print(mmyTestList)

myTestList2 = [letter for letter in myTestString]
print(myTestList2)

myTestList3 = [x for x in 'some word']
print(myTestList3)

myTestList4 = [x for x in range(0,11)]
print(myTestList4)

myEvenSquareList = [x for x in range(0,11) if x%2 == 0]
print('A Even Square list')
print(myEvenSquareList)

print('You can use if else in list comprehensions.')
evenOddResult = [x if x%2==0 else 'ODD' for x in range(0,21)]