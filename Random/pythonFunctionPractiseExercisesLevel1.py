print('Python Practice Exercises Level 1 Problems')
print('#'* 10)
print()
print('OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name')

def old_macdonald(name):
    firstHalf = name[:3]
    secondHalf = name[3:]
    return firstHalf.capitalize() + secondHalf.capitalize()

print(old_macdonald('macdonald'))

print()
print('MASTER YODA: Given a sentence, return a sentence with the words reversed')

def master_yoda(text):
    wordlist = text.split()
    reversedWordList = wordlist[::-1]
    return ' '.join(reversedWordList)

print('Master Yoda said')
print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print()
print('ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200')
print('abs(num) returns the absolute value of a number')

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(90))
print(almost_there(150))