# Q1
def primeNumber1():
    list = []
    for num in range(50, 101):
        counter = -1
        for div in range(2, num//2+1):
            if num % div == 0:
                counter = 1
        if counter != 1:
            list.append(num)
    return list

prime = primeNumber1()
for num  in prime:
    print(num, end=" ")

print("")
print("---")

# Q1.1
def primeNumber2():
    for num in range(50, 101):
        counter = -1
        for div in range(2, num//2+1):
            if num % div == 0:
                counter = 1
        if counter != 1:
            print(num, end=" ")

primeNumber2()


print("")
print("---")

# Q2
def oddIndex(list):
    for index in range(0, len(list)-1):
        elements = list[index]
        if elements % 2 != 0:
            print(index, end=" ")
        else:
            continue

oddIndex([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])


print("")
print("---")

# Q3
def getArguments(name, age):
    print(f"Name: {name}\nAge: {age}")

getArguments("teckann", 18)


print("---")

# Q4
def staff(name, salary = 9000):
    print(f"Hi {name}, your salary is {salary}")

staff("teckann", 5000)
staff("teckann")


# Q5
def outer(a, b):
    def inner():
        return (a+b)
    
    num = inner()
    return (num + 5)

print(outer(10, 12))


print("---")

# Q6
def even(start_with, end_with):
    for even in range(start_with, end_with + 1):
        if even % 2 == 0:
            print(even, end=" ")
        else:
            continue

even(50, 100)

print("")
print("---")

# extra
def first_last_name(full_name):
    list = full_name.split(" ")
    first_name = list[0]
    last_name = list[1]
    print(f"First: {first_name}\nLast: {last_name}")
    
first_last_name("Teck Ann")
