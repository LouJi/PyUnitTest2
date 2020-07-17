from math import *

def add (x,y):
    #Add function
    if type(x) in [bool]:
        raise TypeError('The operands must be a real number')
    if type(y) in [bool]:
        raise TypeError('The operands must be a real number')
    #if type(x, y) not in  [int, float, str]:
        #raise TypeError('The operands must be a real number')
    return x + y

def subtract (x, y):
    #Subtract  function
    if type(x) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    if type(y) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    #if type(x, y) not in  [int, float]:
        #raise TypeError('The operands must be a real number')
    return x - y

def multiply(x,y):
    #Multiply function
    if type(x) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    if type(y) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    #if type(x, y) not in  [int, float]:
        #raise TypeError('The operands must be a real number')
    return x * y

def divide (x,y):
    #Dividefunction
    if type(x) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    if type(y) not in  [int, float]:
        raise TypeError('The operands must be a real number')
    if y == 0:
        raise ValueError ('Cannot divide by zero.')
    return x/y

def containMethod1 (x):
    #if a string contains a value prints True or False
    if type(x) not in [str]:
        raise TypeError('Input must be a string.')
    str1= 'Hello there, this is a example.'
    return x in str1

def  containMethod2 (x):
    #check id a string contains a value. Print start index or -1 if does not contain.
    if type(x) not in [str]:
        raise TypeError('Input must be a string.')
    str2= 'No fear, this too is an example.'
    return str2.find(x)

    #if str2.find(x) == -1
