# Q1
for i in range(1,151):
    if i > 100:
        break
    print(i, end=",")
print("")


print('---')

# Q2
for i in range(1,11):
    result = i * i * i
    print(f"cube of number {i} = {i} x {i} x {i} = {result}")


print("---")

# Q3.1
output = "& "
count = 10
for i in range(1,20):
    if i <= 10:
        result = output * i
        print(result)

    else:
        count -= 1
        i -= count
        result = output * count
        print(result)


print("---")

# Q3.2
output = "& "
for i in range(1,20):
    row = 20
    if i <= 10:
        print(output * i)

    else:
        row -= i
        print(output * row)
    

print("---")

# Q4
print("Python: RM 225")
print("DBase: RM 320")
python = int(input("Quantity of Python: "))
DBase = int(input("Quantity of DBase: "))
total_quantity = python + DBase

python_origin_price = 225 * python
DBase_origin_price = 320 * DBase
total_price = python_origin_price + DBase_origin_price

if 0 < total_quantity <= 3:
    discount = 0.05

elif 4 <= total_quantity <= 10:
    discount = 0.10

else:
    discount = 0.20

print("")
print("Receipt")
print("----------------------")
after_discount_price = total_price - (total_price * discount)
print(f"Quantity of Python: {python}")
print(f"Quantity of DBase: {DBase}")
print(f"Total Price: RM {total_price}")
print(f"Discount: " + str(discount * 100) + " %")
print(f"Amount Should Pay: RM {after_discount_price}")