#simple python program
name = input('What is your name? ')
print('Hello ' + name + '!')
age = input('What is your age? ')
print(f"That's great, {name}. So you are {age} years old!")

temperature = float(input('What is the temperature outside? '))
if temperature > 30:
    print('Thats hot!')
else:
    print('Thats mild!')

print(name.upper())
someoneBday = input('Whos birthday is it today? ')
#Functions
def happyBirthday(name):
    print(f'Happy Birthday {name}!')

happyBirthday(someoneBday)