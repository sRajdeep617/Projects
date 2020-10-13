import random
print('Aloha! ')
ch=input('Do you want to start the dice simulator? ')
if(ch.lower()=='no'):
    print('You have logged out of the simulator')
else:
    print('Welcome to the Dice Simulator Amigo!')
    #its an rng game
    while(ch.lower()=='yes'):
        number=random.randint(1,6)

        if(number=='1'):
            print("----------")
            print("|        |")
            print("|    O   |")
            print("|        |")
            print("----------")
        elif(number=='2'):
            print("----------")
            print("|        |")
            print("| O    O |")
            print("|        |")
            print("----------")
        elif(number=='3'):
            print("----------")
            print("|    O   |")
            print("|    O   |")
            print("|    O   |")
            print("----------")
        elif(number=='4'):
            print("----------")
            print("|O      O|")
            print("|        |")
            print("|O      O|")
            print("----------")
        elif number == 5:
            print("----------")
            print("| O    O |")
            print("|    O   |")
            print("| O    O |")
            print("----------")
        else:
            print("----------")
            print("| O    O |")
            print("| O    O |")
            print("| O    O |")
            print("----------")
        ch=input('Do you want to continue? ')
    print('Adios Amigo!')
    print('Hope you enjoyed!')
    