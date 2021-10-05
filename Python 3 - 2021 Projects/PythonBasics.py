# 21 Sep 2021 - Python for Beginners Udemy Refresher 
print("Hello Steve, its been a while!")
print("Lets do some simple arithmetic math.")
print(400 + 20)
print("To the power of **")
print("Remember modulo % - this finds remainders (useful for odds or evens, etc)")
print(10 ** 3)
print('\n')
print('-' * 20)
print('Variables')
print('-' * 20)
example_var = "Variable names are case sensitive and cannot start with a number. They can only contain alpha-numeric characters (A-z, 0-9 and _)"
print(example_var)
print('snake_case is preferred over camelCase')

"""
Multi
Line
Comment
"""

'''
Can use single or double quotes 
for multi-line commnets
'''
print('\n')
print('-' * 20)
print('Playing with Strings')
print('-' * 20)
print('Let\'s try escape with \\ \n\\n is for new line.')
statement = '''
Printing
Multi
Line
Statement
'''
print(statement)
name = 'Neo'
print('Hello ' + name)
year = 2021
print('The year is ' + str(year))
print('Follow the white rabbit {}'.format(name))
day = '5th'
month = 'November'
# More secure to assign a variable name in the format params
print('Remember remember the {first} of {last}...'.format(first=day, last=month))
# Better version of the format statement f''
hello_statement = f'Hello again {name}'
print(hello_statement.upper())
string_methods = ''' 
Useful string methods 
.capitalize() - capitalize first letter of string
.count('a') - count how many times a is in the string
.endswith('a') - true or false to check if the string ends with a
.isdigit() - true or false to determine if the string is an digit
'''
print(string_methods)
print('\n')
print('Getting user input')
username = input('Enter your name: ')
print(f'Hello {username}')
print('\n')
print('-' * 20)
print('Lists - collections of data')
print('-' * 20)
my_list = [1,2,3,4,5]
my_list_2 = [6,7,8,9,10]
print(my_list)
cat_list = ['Tiger','Lion','Puma']
print(cat_list)
print('The king of the jungle is a ' + cat_list[1])
print('To get the last element of a list you can use -1, my_list[-1]')
print('The length of the cat_list is: ' + str(len(cat_list)))
print('\n')
print('Slicing Lists')
print('Slice the first two elements of an list [0:2] - ' + str(my_list[0:2]))
new_list = my_list + my_list_2
print('Print only every 2nd increment [0:-1:2] - ' + str(new_list[0:10:2]))
print('Adding and removing elements from an list')
print('.append(\'something\') - add to the end of an list')
print('.insert(index, new_value) - insert into an list')
print('.remove(value) - find value and remove the first occurrence of it from the list')
print('.pop(index) - remove element based on index value')
print('.reverse() - reverse the list')
print('.sort() - sort the list')
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(len(nested_list))
print(f'My nested list has {nested_list[0][2]} lists in it.')
print('\n')
print('-' * 20)
print('Booleans - True or False')
comparison_operators = '''
Comparison Operators
== Equals
!= Not Equals
> Greater Than
< Less Than
>= Greater than or equal to
<= Less that or equal to
'''
print(comparison_operators)
print('-' * 20)
print(2 < 3)
print('\n')
print('-' * 20)
print('Flow Control: If Statements')
print('If, elif and else')
print('-' * 20)

if username.lower() == 'neo':
    print(f"Hello {username}, you are the one.")
elif username.lower() == 'trinity':
    print(f'{username}, you will fall in love with the one.')
else:
    print(f"Unfortunately {username}, you are not the one.")

print('\n')
print('-' * 20)
print('Loops')
print('Two different types of loops, FOR and WHILE')
print('-' * 20)
print('For Loops: Iteration!')
new_numbers = [1,2,3,4,5]

for x in new_numbers:
    print(x)

sum_of_loop = 0
for x in range(3,6):
    sum_of_loop += x
    print(sum_of_loop)

co_workers = ['Gin','Ben','Tom', 'Bob']
for y in co_workers:
    if y == 'Tom':
        print('Tom is my only real co-worker')
        break
    else:
        print(f'{y} is not an real co-worker')

print('While Loops!')
x = 0
while x < 10:
    x += 1
    if x == 5:
        print('Half way there...')
        # Notice how it does not print 5 and jumps over this iteration
        continue
    print(x)
else:
    print('x is now equal or larger than 10')


print('\n')
print('-' * 20)
print('Functions')
print('-' * 20)

""" my_new_list = [1,2,3,4]
my_new_list.append(5)
print(my_new_list) """


def my_function(first_name):
    print(f"Hello! {first_name}")
    print("Printing from an function")


my_function('Neo')

# passing in multiple arguments of unknown argument length
def my_function_2(*bunch_of_data):
    print(bunch_of_data[-1])


my_function_2(1,2,3,4,5)


def my_function_3(high_number, low_number):
    print(high_number)
    print(low_number)

my_function_3(low_number=1, high_number=9)


# assigning default values
def my_function_4(country = 'Somewhere in the world.'):
    print(country)


my_function_4()
my_function_4('United Kingdom')


def my_function_5(num_one, num_two):
    return num_one * num_two

print(my_function_5(5,5))

# Fibonacci Sequence in non-recursive mannor
def fib_seq(amount):
    n1 = 0
    n2 = 1

    if amount <= 0:
        print('Please change to a positive int')
    elif amount == 1:
        print('Fib seq: ')
        print(n1)
    else:
        print('Fib seq: ')
        count = 0
        while count < amount:
            print(n1)
            fib_sum = n1 + n2
            n1 = n2
            n2 = fib_sum
            count += 1

fib_seq(13)

# Possible for an function to call itself - this is an recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print('Factorial of 5 is: ' + str(factorial(5)))


def fib_seq_recursive(amount):
    if amount == 0:
        return 0
    elif amount == 1:
        return 1
    else:
        return fib_seq_recursive(amount - 2) + fib_seq_recursive(amount - 1)


print(fib_seq_recursive(13))


print('\n')
print('-' * 20)
print('Advanced String methods')
print('-' * 20)

greetings = "Welcome, to the Python world!"
#indexing 
#print(grettings[0])

#Slicing
print(greetings[0:7])

#Length of string
print(len(greetings))

# return a list seperated by comma
#print(greetings.split(','))

# Find and return index
#print(greetings.find('Python'))

# Join two strings with some conditions - useful for time strings
print(greetings, ':'.join('abcdefg'))

password = 'abc123!  '
# strip off whitespaces with strip()
print(password.strip())

# replace
new_greetings = greetings.replace('Welcome to', 'Hello there and welcome to')
print(new_greetings)


print('\n')
print('-' * 20)
print('Dictionaries')
print('A dictionary is a collection which is unordered, changeable and indexed. In python they are writing with curly brackets, and have key, value pairs')
print('-' * 20)

user_dict = {
    'first_name': 'Thomas',
    'last_name': 'Anderson',
    'alias' : 'Neo'
}

print(user_dict)
print(user_dict.get('alias'))
# add to dictionary
user_dict['lover'] = 'Trinity'
print(user_dict)
print(len(user_dict))
# can remove either with pop or popitem which deletes the last value
user_dict.pop('lover')
user_dict.popitem()
# use delete with caution as you can delete the whole dictionary
del user_dict['last_name']
# remove all key value pairs with .clear()

for x, y in user_dict.items():
    print(x, y)

# Copying dictionary
# cant directly copy as it will copy the memory address
# this is the proper way to copy
dict2 = user_dict.copy()
print(dict2)

# can create nested dictionaries
family = {
    'child1': {
        'firstname': 'John'
    },
    'child2' : {
        'firstname': 'Merry'
    }
}

print('\n')
print('-' * 20)
print('Sets amd Tuples')
print('A tuple is a collection which is ordered and unchangeable. In python they are writing in round parentheses.')
print('-' * 20)

my_tuple = (1,2,3,4,5)
print(my_tuple)
print('Cant change values in a tuple!')

sets = """
Sets!

- Sets are a type of data structure like lists
- Lists are slightly faster than sets when you just want to iterate over values
- Sets, however, are significantly faster that an lists if you wna to check if an item is contained within it. They can only contain unique items though.
- Used most often to remove duplicates, and to check if item exists
- Sets are unordered
"""
print(sets)

my_set1 = {'apples','bananas','oranges', 'melons'}
print(my_set1)
print('melons' in my_set1)
print('grapes' in my_set1)
for x in my_set1:
    print(x)

# Two ways to remove items in an set .remove('something') - will error if item does not exist
# .discard('apples') - does not error out if item does not exist

# can combine sets
set_one = {1,2,3,4,5}
set_two = {6,7,8,9,10}
set_three = set_one.union(set_two)
# add to set
set_three.add(11)
# add more than 1 item
set_three.update([12,13])

print('\n')
print('-' * 20)
print('Importing Modules and Standard Library')
print('-' * 20)
import random as ran

types_of_drinks = ['Soda','Water','Coffee','Tea']
print(str(ran.randint(1,10)) + ' - ' + ran.choice(types_of_drinks))