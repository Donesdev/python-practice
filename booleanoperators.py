'''bool type has two possible values: True or False.
They can also be represented by numbers in Python, with
False equal to 0 and True == to 1'''

""" In addition to the bool type, Python provides three boolean 
operators ( also called logical operators): and , or , and not
Boolean operators allow us to build and combine more complex boolean
inputs and return boolean results.
"""

""" A Boolean operator that works with only one argument is not.
The not operator is a reserved keyword and boolean operator that works
with one argument and returns the opposite thuth value of the argument. 
This means that if False is passed to the operator, True is returned. If
True is passed to the operator, False is returned. 
"""

# Example to compare the two values when they are equal

# num = 1
# if num==1:
#     print('True')
# else:
#     print('False')

# Here we compare two values when they are not equal, which should return False

# num =1 
# if num ==0:
#     print('True')
# else:
#     print('False')

# Now let's try the same example, but adding in the not boolean operator. 

# num=1
# if not (num == 1):
#     print('True')
# else:
#     print('False')

# num = 1
# if not (num == 0):
#     print('True')
# else:
#     print('False')

"""
Now for the other two boolean operator types and and or.
These two operators take multiple arguments.
The and operator is a reserved keyword and boolean operator that takes
two arguments and returns a boolean value of False unless both inputs
are True.  
"""

"""
Python boolean operators such as and and or use an evaluation method
called short-circuit evaluation. Python reads code from left to right.
Python will start evaluating the left operand and when it detects
that there is nothing to be gained by evaluation and does not do the 
computations in the res of the logical expression. This is called short-
circuit evaluation, When the evaluation of a logical expression stops because
the overall value is already known.
"""

# Example

# num1= 1
# num2= 2
# if num1 == 0 and num2 ==0:
#     print('A is False, B is False: True')
# else:
#     print('A is False, B is Flase: False')

# if num1 == 0 and num2 == 2:
#     print(' A is False, B is True: True')
# else:
#     print('A is False, B is True: False')

# if num1 == 1 and num2 == 0:
#     print('A is True, B is False: True')
# else:
#     print('A is True, B is False: False')

# if num1 == 1 and num2 == 2:
#     print('A is True, B is True: True')
# else:
#     print('A is True, B is True: False')

"""
The or boolean operator outputs True if either iput is True(or both).
It only ouputs False if both inputs are set to False. 
"""

# num1 = 1 
# num2 = 2

# if num1 == 0 or num2 == 0:
#     print('A is False, B is False: True')
# else:
#     print('A is False, B is False: False')

# if num1 == 0 or num2 == 2:
#     print('A is False, B is True: True')
# else:
#     print('A is False, B is True: False')

# if num1 == 1 or num2 == 0:
#     print('A is True, B is False: True')
# else:
#     print('A is True, B is False: False')

# if num1 == 1 or num2 == 2:
#     print('A is True, B is True: True')
# else:
#     print('A is True, B is True: False')

a = 5
b = 15
c = 10
d = 0
if a > b:
    d = 4
elif b > c:
    d = 5
else:
    d = 6
print(d)
