'''
Errors and Exceptions (Try catch)
'''

# Cant divide by 0
try:
    #x = 10 * (1/0)
    #print(x)
    # Causes type error
    y = '2' + 2

except ZeroDivisionError as e:
    print(f'{e}: Cannot divide by 0!')

except TypeError as t:
    print(f'{t}: Type error')

except Exception as e:
    # Will no get caught in this case as the other two specific expections will catch it first.
    # Parent exception
    print(f'Error was thrown: {e}')
finally:
    print('Finally shows no matter what, even if no errors')