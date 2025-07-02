# Q1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum of the two given numbers is: " + str(sum))


print("---")

# Q2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))

average = round(((num1 + num2 + num3 + num4 + num5)/5), 2)
print("The average of the two given numbers is: " + str(average))


print("---")

# Q3
import math

radius = float(input("Enter radius value: "))
pai = math.pi

area = round((pai * (radius ** 2)), 2)
circumference = round((2 * pai * radius), 2)

print("The area value is: " + str(area))
print("The circumference value is: " + str(circumference))


print("---")

# Q4
sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / (5 * 100)) * 100
print("The total marks is: " + str(total))
print("The overall percentage is: " + str(percentage) + "%")


print("---")

# Q5
Basic_pay = float(input("Basic Pay: RM "))
Grade_pay = Basic_pay * 2
DA = Basic_pay * 0.70
TA = 200
HRA = Basic_pay * 0.20

salary = round((Grade_pay + DA + TA + HRA), 2)
print("Salary : RM " + str(salary))
