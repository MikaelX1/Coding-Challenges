#Create a function that takes voltage and current and returns the calculated power.
#Example : circuitPower(230, 10) ➞ 2300


def power(x,y):
    pow = x * y
    return pow

vol = int(input("Enter the Voltage:"))
cur = int(input("Enter the Current:"))

print("The Power is:", power(vol,cur))
