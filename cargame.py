# Car Game

# > help
# start - to start the car
# stop - to stop he car
# quit - to exit

# term dry is used i.e Don't Repeat Yourself

is_started = False
command = ""
while True:
    command = input('> ').lower()
    if command == 'help':
        print('start - to start the car')
        print('stop - to stop he car')
        print('quit - to exit')
    if command == 'start':
        if is_started:
            print('car is already on its way ')
        else:
            print('car started ')
            is_started = True

    elif command == 'stop':
        if is_started:
            print('car stopped ')
            is_started = False
        else:
            print('car has not started yet, how it can be stopped !!! ')

    elif command == 'quit':
        break
    else:
        print("I don't understand !!!")

else:
    print('Car Game Quit')

