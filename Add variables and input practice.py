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

    
   
