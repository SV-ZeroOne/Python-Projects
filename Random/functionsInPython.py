#Python Functions
#starts with defining the name_of_function():
#   doSomethingInFunction

#if no params is given then Default is applied
def name_of_function(argument='Default'):
    '''
    Docstring explains function.
    '''
    print(f"Hello {argument}")

name_of_function()
name_of_function("Steve")
print()

def adding_function(num1, num2):
    '''
    DOCSTRING: Information about this function. It adds 2 things together.
    INPUT: num1, num2
    OUTPUT: num1 + num2
    '''
    return num1 + num2

returnResult = adding_function(400,20)
print(returnResult) 
print()
help(adding_function)

#find out if the word dog is in a string?
#noobie way
def dog_check(myString):
    if 'dog' in myString.lower():
        return True
    else:
        return False

print(dog_check('I have 3 big dogs'))

#better way - statement below retruns a boolean value
def cat_check(myString):
    return 'cat' in myString.lower()

print(cat_check('I wish I had a fat cat.'))

def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

import math

def is_prime2(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True