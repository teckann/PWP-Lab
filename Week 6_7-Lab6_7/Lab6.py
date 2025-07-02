# Q1
i = 1

while i == 1:
    name = str(input("Please enter your name: "))
    mark = int(input("Please enter your marks: "))

    if mark >= 50:
        print(f"{name}, you have passed the module.")

    else:
        print(f"{name}, you have failed the module.")

    print("Continue (1), Exit (2)")
    i = int(input(">>> "))


print("---")

# Q2
valid_status = 1
mark_status = "Pass"
mark = int(input("Enter your marks: "))

if 0 <= mark <= 49:
    grade = "F"
    mark_status = "Fail"

elif 50 <= mark <= 59:
    grade = "D"

elif 60 <= mark <= 69:
    grade = "C"

elif 70 <= mark <= 79:
    grade = "B"

elif 80 <= mark <= 100:
    grade = "A"

else:
    valid_status = 0

if valid_status == 1:
    print(f"Your grade is: {grade}")
    print(f"Your status is: {mark_status}")

elif valid_status == 0:
    print("Invalid Entry")



print("---")

# Q3
i = 1

while i <= 20:
    print(i, end=",")
    i += 1
print("")


print("---")

# Q4
i = 0

while i <= 38:
    print(i, end=",")
    i += 2
print("")


print("---")

# Q5
i = 0

while i <= 9:
    i += 1
    result = 7 * i
    print(f"7 x {i} = {result}")

print("...")

for i in range(1, 11):
    result = 7 * i
    print(f"7 x {i} = {result}")