#Example 
""" Here is a sample program that convert a Fahrenheit tamperature to a 
Celsius Temperature:
"""

# inp = input('Enter Fahrenheit Temperature: ')
# fahr = float(inp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

"""
But what if we tried to execute this code with invalid input like not a number
"""

"""
There is a conditional execution structure built into Python to handle types of
expected and unexpected errors called the "try/except" statement. 
The idea of the try and except statement is that if you know 
that some sequence of instruction(s) may have a problem, you can add
some statements to be executed if an error occurs. These extra statements
(the except block) are ingnored if there is no error. 

You can think of the try and except feature in python as an "insurance policy"
"""
# Example 

# inp = input(' Enter Fahrenheit Temperature:')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('You did not enter in a number. Please enter a number next time')

# grade = 71
# if grade > 90:
#     print("You got a A")
# elif grade > 80:
#     print("You got a B")
# elif grade > 70:
#     print("You got a C")
# elif grade > 60:
#     print("You got a D")
# elif grade <= 60:
#     print("You got a F")
# print("we are done!")

# num = int(input("Enter your age: "))
# if num ==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# myVar1 = '3'
# myVar2 = '2'
# lines = int(myVar1) + int(myVar2)
# myStr = myVar2 + ' ' + myVar1 + '\n'
# result = myStr * lines + str(lines)
# print(result)

a = 10
b = 2
c = 3
d = 0
if a > b:
    d = 4
else:
    if a > c:
        d = 5
print(d)