import string
print('Python Homework Problems')
print('#'* 10)
print()
print('Write a function that computes the volume of a sphere given its radius.')

def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)

print(vol(2))
print()
print('Write a function that checks whether a number is in a given range (inclusive of high and low)')

def ran_check(num,low,high):
    if num in range(low, high):
        print("{} is in the range".format(str(num)))
    else:
        print("The number is outside the range.")

ran_check(5,2,7)

def ran_bool(num,low,high):
    return num in range(low,high)

print(ran_bool(3,1,10))
print()
print('Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.')

def up_low(s):
    d={"upper":0, "lower":0}
    for c  in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print(f'Original String : {s}')
    print(f'No. of Upper case characters : {d["upper"]}')
    print(f'No. of Lower case characters : {d["lower"]}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

print()
print('Write a Python function that takes a list and returns a new list with unique elements of the first list.')

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print()
print('Write a Python function to multiply all the numbers in a list.')
def multiply(numbers):  
    total = numbers[0]
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,-4]))
print()

print('Write a Python function that checks whether a passed in string is palindrome or not.')
print('Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.')
def palindrome(s):
    return s == s[::-1]


print(palindrome('helleh'))
print()
print('Write a Python function to check whether a string is pangram or not.')
print('Note : Pangrams are words or sentences containing every letter of the alphabet at least once.')
print('For example : "The quick brown fox jumps over the lazy dog"')

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))