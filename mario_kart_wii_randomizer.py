from sys import exit
from time import sleep
from mario_kart_wii_randomizer_functions import Small_Med_Heavy_Class_Picker as randomizer


"""
Program Desc:

Randomly chooses a character and vehicle for you in Mario Kart Wii!

"""

print("Mario Kart Wii Character and Vehicle Randomizer")

x = input("Begin? Y/N: ")
x = x.upper()

if x == "N":
    print("Goodbye...")
    exit()

else:
    pass

num = 1

while True:

    if num == 5:
        print("=============")
        x = input("Do you want to run the randomizer again? Y/N: ")
        x = x.upper()

        if x == "Y":
            num = 1
            continue
        else:
            print("Goodbye...")
            break

    else:
        print("=============")
        print("Player", num)
        randomizer()
        num += 1
        sleep(0.3)
