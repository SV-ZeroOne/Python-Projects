print('#'*10)
print("Nested Statements and Scope")
print('#'*10)
print()
y = 25

def printer():
    y = 50
    return y

print(y)
print(printer())

'''
LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()

x = 50
print(x)
def func():
    global x
    print(f'x is {x}')
    x = "NEW VALUE"
    print('I just LOCALLY changed GLOBAL x to', x)

func()