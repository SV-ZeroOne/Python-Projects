print('#'*10)
print("Lambda Expressions, Map, and Filter")
print('#'*10)
print()
print('Map Function')
print('The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:')
print('map(func, *iterables)')

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# To get the results, either iterate through map() 
# or just cast to a list

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Steve', 'James', 'Sally', 'Even']
print(list(map(splicer, names)))

print()
print('Filter Function')
print('The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.')
print()
def check_even(num):
    return num%2==0

mynumbers = [1,2,3,4,5,6]


print(list(filter(check_even,mynumbers)))
for n in filter(check_even, mynumbers):
    print(n)

print()

def squareAgain(num):
    result = num ** 2
    return result

#turn the above into a lambda expression
newSquare  = lambda num: num ** 2
print(newSquare(6))

print(list(map(lambda num: num**2,mynumbers)))
#lambda expression of check_even.
print(list(filter(lambda num:num%2==0, mynumbers)))

print(list(map(lambda x:x[0], names)))
