# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# loops
# while loop

# while condition:  while this condition is true following code will execute
# ......

i = 0
while i < 5:
    i += 1
    print(i)
print('DONE')

i = 1
while i <= 5:
    print(i * '*')
    i += 1
print('DONE')

i = 1
while i <= 5:
    print(math.factorial(i))
    i += 1
print('DONE')


#  Guess Game

secret_number = 4
guess_limit = 3
guess_count = 1
while guess_count <= guess_limit:
    guess_count += 1
    guess = int(input("Guess: "))
    if guess == secret_number:
        print(f"You won!!! {secret_number} is secret number")
        break # to terminate the loop
else: # when all iterations are done , similar to if else
    print("You lose, Try next time")


#  Guess Game

secret_number = 4
number_of_iteration = 3
i = 1
while i <= number_of_iteration:
    i += 1
    guess = int(input("Guess: "))
    if guess == secret_number:
        print(f"You won!!! {secret_number} is secret number")
        break # to terminate the loop
    if i >= 4:
        response = input("You want to try again Y/N: ")
        if response.lower() == 'y':
            i = 0

