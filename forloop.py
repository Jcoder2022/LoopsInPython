# accessing each character in a String

for item in 'Python':
    print(item);

# List is represented with [], it may be list of numbers, customers, products
# List of numbers
for item in [1, 2, 3, 4]:
    print(item)

# List of names
items = ['saboor', 'sadia', 'jalal', 'Aliya']
for item in items:
    print(item)

# when we wanna iterate over 1000 numbers, at this point we use range function
# range method creates new object for each number, output will be 0 to 9, 10 will not be included
for item in range(10):
    print(item)

# we may also provide range like from 5 to 9 will be output
for item in range(5, 10):
    print(item)

# range function can optionally take step in a function

for item in range(0, 10, 2):  # will display all even numbers
    print(item)

# total cost of all items in shopping cart

prices = [10.98, 20.78, 1.98, 3.86]
total_price = 0
for price in prices:
    total_price += price
print(f"Total price os items in shopping cart is {total_price}")

# Nested loop
for x in range(4):
    for y in range(2):
        print(f'({x},{y})')

# Challenge

#  xxxxx
#  xx
#  xxxxx
#  xx
#  xx

# Nested loop
for x in range(3):
    for y in range(2):
        if x == y:
            print('x' * 5)
        else:
            print('x' * 2)

print("-------------------------------------")
#  xx
#  xx
#  xx
#  xx
#  xxxxxx

for x in range(3):
    for y in range(2):
        if x == 2 and y == 1:
            print('x' * 5)
        else:
            print('x' * 2)
