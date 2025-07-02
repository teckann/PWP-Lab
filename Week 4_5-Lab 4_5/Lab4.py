# Q1
print("Please enter your reading as INTEGER")
max_tem = int(input("Maximum Temperature Reading: "))
min_tem = int(input("Minimum Temperature Reading: "))

average = round((max_tem + min_tem) / 2)

print("Average Temperature: ", average)


print("---")

# Q2
bmi = float(input("Please enter your BMI: "))

if bmi < 18.5:
    print("Underweight")

elif 18.5 < bmi < 20.0:
    print("Normal")

elif 20.0 < bmi < 30.0:
    print("Overweight")

else:
    print("Obese")


print("---")

# Q3
status = 1
name = input("Please enter your name: ")
purchase_amount = float(input("Please enter your purchase amount: "))
print("")
print("0 : Tax Exempted (0%)")
print("1 : Good Tax Only (6%)")
print("2 : Good Tax and Service (16%)")
tax_code = int(input("Please enter your tax code: "))

if tax_code == 0:
    tax_status = "Tax Exempted (0%)"
    total_amount_due = round((purchase_amount * 0) + purchase_amount,2)

elif tax_code == 1:
    tax_status = "Good Tax Only (6%)"
    total_amount_due = round((purchase_amount * 0.06) + purchase_amount,2)

elif tax_code == 2:
    tax_status = "Good Tax and Service (16%)"
    total_amount_due = round((purchase_amount * 0.16) + purchase_amount, 2)

else:
    status = 0

if status == 1:
    print("")
    print("Customer's Name: " + name)
    print("Purchase Amount: RM" + str(purchase_amount))
    print("Tax Imposed: " + tax_status)
    print("Total Amount Due: RM" + str(total_amount_due))

else: 
    print("")
    print("Please select the correct tax code!")


print("---")

# Q4
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    diff = num1 - num2
    if diff > 0:
        print("The largest number: " + str(num1))
        print("Difference between these two numbers: " + str(diff))

elif num2 > num1:
    diff = num2 - num1
    if diff > 0:
        print("The largest number: " + str(num2))
        print("Difference between these two numbers: " + str(diff))

else:
    print("Please enter different number value!")


print("---")

# Q5
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print("Calculator: \n\t 1. Add \n\t 2. Subtract \n\t 3. Multiply \n\t 4. Divide")
status = int(input("Please select one operation: "))

if status == 1:
    add = num1 + num2
    print("Answer: " + str(add))

elif status == 2:
    subtract = num1 - num2
    print("Answer: " + str(subtract))

elif status == 3:
    multiply = num1 * num2
    print("Answer: " + str(multiply))

elif status == 4:
    divide = num1 / num2
    print("Answer: " + str(divide))

else:
    print("Please select the correct operation!")