import random
#Python project A

randomNumber = random.randint(1, 99)
print(randomNumber)
guess = int(input('Enter a number from 1 to  99: '))

while randomNumber != guess:
    print
    if guess < randomNumber:
        print('Your guess is to low')
        guess = int(input('Enter a number from 1 to  99: '))
    elif guess > randomNumber:
        print('Your guess is to high')
        guess = int(input('Enter a number from 1 to  99: '))
    else:
        print('You guessed the right number!')
        break
    print

