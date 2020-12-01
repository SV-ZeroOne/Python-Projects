#Statements Assessment Test
print('#'*10)
print('Udemy Python Bootcamp')
print('Statements Assessment Test')
print('#'*10)
print("Use for, .split(), and if to create a Statement that will print out words that start with 's'")
st = 'Print only the words that start with s in this sentence'
myWords = []
myWords = st.split()
mySwords = []
for word in myWords:
    if word[0].lower() == 's':
        mySwords.append(word)
print(mySwords)
#better logic from solution
for word in st.split():
    if word[0] == 's':
        print(word)

print()
print('Use range() to print all the even numbers from 0 to 10.')
betterEvenList = list(range(0,11,2))
myEvenList = [x for x in range(0,11) if x%2 == 0]
print(myEvenList)
print()
print('Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.')
myListComp = [y for y in range(0,51) if y%3 == 0]
print(myListComp)

print()
print('Go through the string below and if the length of a word is even print "even!"')
someSentence = 'Print every word in this sentence that has an even number of letters'
print(someSentence)
for word in someSentence.split():
    if len(word) % 2 == 0:
        print(f'Word : "{word}" is even!') 

print('Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".')
for num in range(0,101):
    if num % 3 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


print('Use List Comprehension to create a list of the first letters of every word in the string below:')
st1 = 'Create a list of the first letters of every word in this string'
myList = [word[0] for word in st1.split()]
print(myList)