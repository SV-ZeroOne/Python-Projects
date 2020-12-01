print('Python Practice Exercises Challenging Problems')
print('#'* 10)
print()
print("SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order")

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0) # code.remove(num) also works

    return len(code) == 1 

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

print()
print("COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number")

def count_primes(num):
    #Check for 0 or 1 input as we dont want to count these
    if num < 2:
        return 0
    
    #2 or greater
    #store our prime numbers
    primes = [2]
    #Counter going up to the input num
    x = 3
    #x  is going through every number up tp input number
    while x <= num:
        #Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else: #Unique to Python is the FOR ELSE statement.
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
print()
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes2(100))
print()
print("PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter")
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')