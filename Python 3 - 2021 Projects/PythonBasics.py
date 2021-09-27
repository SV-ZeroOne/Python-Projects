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