# Lab 8 (Set 1)
# Q1
def sum(x, y):
    sum = x + y
    return sum

x = int(input("Enter fisrt number: "))
y = int(input("Enter second number: "))

sum = sum(x, y)
print(f"Sum of the given two numbers is: {sum}")


print("---")

# Q2
def average(x, y, z):
    average = (x + y + z) / 3
    return average

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

average = average(x, y, z)
print(f"Average of the given three numbers is: {average}")


print("---")

# Q3
def choice():
    print("Calculator Program\n\t1. ADD\n\t2. SUBTRACT\n\t3. MULTIPLY\n\t4. DIVIDE\n\t5. EXIT")
    choice = int(input("Choose the operation from the given options: "))
    return choice

def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    result = x / y
    return result

# main logic
status = True
while status == True:
    ch = choice()

    if ch == 5:
        print("Exited")
        status = False
        break

    x = int(input("Enter first number: "))
    y = int(input("Enter the second number: "))
    print("")

    if ch == 1:
        result = add(x, y)
    elif ch == 2:
        result = subtract(x, y)
    elif ch == 3:
        result = multiply(x, y)
    elif ch == 4:
        result = divide(x, y)
    else:
        print("Please enter correct choice number")
        status = False
    print(f"Result: {result}")

print("---")

# Q4
import math
pi = round(math.pi, 5)

def diameter(radius):
    result = round(2 * radius, 2)
    return result

def circumference(radius):
    result = round(2 * pi * radius, 2)
    return result

def area(radius):
    result = round(2 * pi * radius ** 2, 2)
    return result

radius = float(input("Please enter the radius: "))

print(diameter(radius))
print(circumference(radius))
print(area(radius))


print("---")

# Q5
def Q5(name, age):
    print(f"Name: {name}\nAge: {age}")

Q5("teckann", 18)