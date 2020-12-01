#Python function practice exercises 

print('LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd')
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0 :
        #Both numbers are even
        #if a < b:
        #    result = a
        #else:
        #    result = b
        return min(a,b)
    else:
        #One or both numbers are odd.
        #if a > b:
        #    result = a
        #else:
        #    result = b
        return max(a,b)


print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

print()
print('ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter')

def animal_crackers(string):
    words = string.lower().split()
    return words[0][0] == words[1][0]

print(animal_crackers('Crazy cat'))
print(animal_crackers('Dog Wolf'))

print()
print('MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False')

def makes_twenty(x,y):
    return x+y==20 or x==20 or y==20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))