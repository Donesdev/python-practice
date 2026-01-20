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
    

    
   
