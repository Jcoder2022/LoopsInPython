# Car Game

# > help
# start - to start the car
# stop - to stop he car
# quit - to exit
is_started = False
simulator = input('> ')
while simulator.lower() == 'help' or simulator.lower() == 'start' or simulator.lower() == 'stop':
    if simulator.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop he car')
        print('quit - to exit')
    if simulator.lower() == 'start':
        if is_started == False:
            print('car started ')
            is_started = True
        else:
            print('car is already on its way ')
    if simulator.lower() == 'stop':
        if is_started == True:
            print('car stopped ')
            is_started = False
        else:
            print('car has not started yet, how it can be stopped !!! ')

    if simulator.lower() == 'quit':
        break
    simulator = input('> ')
else:
    print('Car Game Quit')