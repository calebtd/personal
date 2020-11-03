import time

batteryCharge = 0.0
doorOpen = False


def dot(x):
    for y in [".", "..", "...", "....", "....."]:
        # use \r for a carriage return, use end='' to prevent new line
        print(f"\r{x}{y}", end='')
        time.sleep(.75)
    print()


def printBatteryCharge():
    print(f"Current battery charge: {batteryCharge * 100}%")


while True:
    command = input('\nCommand please: ').lower()

    if command == 'check battery':
        printBatteryCharge()

    elif command == 'charge battery':
        batteryCharge = 1
        printBatteryCharge()

    elif command == 'open door':
        if doorOpen:
            print('Door already open.')
        elif batteryCharge == 0:
            print("Battery is dead. Can't open door.")
        else:
            dot('Door opening')
            doorOpen = True

    elif command == 'shoot laser':
        if batteryCharge < .6:
            print("Your battery must be at 60% capacity to fire the laser.")
        elif not doorOpen:
            print("The door must be open to fire the laser.")
        else:
            print("Kapow!!! Laser fired.")
            batteryCharge -= .2
            printBatteryCharge()

    else:
        print('Invalid Input')

    if batteryCharge >= .05:
        batteryCharge -= 0.05
    else:
        batteryCharge = 0
