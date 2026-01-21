name = input("What's your name ?")
age = input("How old are you ?")

print("Hello", name)
print("You are", age, "Years old")



name = input("What's your name ?")
age = int(input("How old are you ?"))

print("Hello", name)
print("You are", age, "Years old")



import re
name = input("What's your name ? ")
age_text = input("How old are you ?")
age_match = re.search(r"\d+", age_text)
age = int(age_match.group() if age_match else "unknown")

print (f"Hello {name}")
print(f"You are {age} years old")


# Pay per rate per hour
hrs = input("Enter work hours")
rate = input("Enter rate per hour")
pay = int(hrs) * float(rate)
print(f'Pay: {pay}')

# Pay with over time being time and half more
hrs = input("Enter hours worked: ")
h = float(hrs)
rate = input("Enter rate per hour: ")
r = float(rate)
regularhours = 40
regularpay = regularhours * r

if h > 40:
    ot = h - regularhours
    otrate = ot * ( r * 1.5)
    otpay = regularpay + otrate
    print(otpay)
    
# same code with the try and except incase the input is not numeric
hrs = input("Enter hours worked: ")
rate = input("Enter rate per hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

regularhours = 40
regularpay = regularhours * r

if h > 40:
    ot = h - regularhours
    otrate = ot * ( r * 1.5)
    otpay = regularpay + otrate
    print(otpay)

# Grade score 
score = input("Enter grade score between 0.0 and 1.0: ")
scoree = float(score)
if scoree >= 0.9:
    print("A")
elif scoree >= 0.8:
    print("B")
elif scoree >= 0.7:
    print("C")
elif scoree >= 0.6:
    print("D")
elif scoree < 0.6:
    print("F")
else:
    print("Enter numeric input between 0.0 and 1.0")

# Computepay with functions and return 
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:" )
r = float(rate)
normalh = 40
normalpay = float(normalh) * float(r)
def computepay(h, r):
    if h > normalh:
        ot = h - normalh
        normalpay = normalh * r
        otpay = ot * r * 1.5
        return normalpay + otpay
    return h * r
 
#No newline at end of file
print("Pay", computepay(h, r))

    
# program that reads numbers until user says 'done'
# Combination of loop with exit mechanisim
# we have some sanity checking of our input
# making sure we have some valid input
# and we catch it and we use continue to loop back up to run 
# the next iteration of the loop
# and we have an accumulator patter and the we can use the 
# accumulated date to print what we want to print

num = 0 # running count
tot = 0.0 # running total
while True :
    sumvalue = input("Enter a number: ")
    if sumvalue == 'done' :
        break
    try:
        floatvalue = float(sumvalue)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num + 1 # counter patter
    tot = tot + floatvalue # accumulating patter where we are adding a value to it
# print('ALL DONE')
print(tot, num, tot / num)

# Start with no numbers seen yet.
largest = None
smallest = None

#Start an infinite loop so we can keep asking for input.
while True:
   
    # Ask the user for input and store it as a string.
    num = input("Enter a number: ")

    # If the user types done, exit the loop.
    if num == "done":
        break

    # Try to convert the input string into an integer.
    try:
        value = int(num)

        # If conversion fails, print an error and skip to the next loop iteration.
    except:
        print("Invalid input")
        continue
        print(num)

    # If this is the first valid number, 
    # or it’s bigger than the current largest, update largest.

    if largest is None or value > largest:
        largest = value

    # If this is the first valid number, 
    # or it’s smaller than the current smallest, update smallest.
    if smallest is None or value < smallest:
        smallest = value

# After the loop ends, print the largest and smallest numbers found.
print("Maximum is", largest)
print("Minimum is", smallest)

    
   
