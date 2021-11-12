import random
temp = "y"

while(temp == "y") :
    no = random.randint(1,6)
    if (no == 1 ):
        print("\t _______")
        print("\t|       |")
        print("\t|   0   |")
        print("\t|_______|")
    if (no == 2 ):
        print("\t _______")
        print("\t|     0 |")
        print("\t|       |")
        print("\t|_0_____|")
    if (no == 3 ):
        print("\t _______")
        print("\t| 0     |")
        print("\t|   0   |")
        print("\t|_____0_|")
    if (no == 4 ):
        print("\t ________")
        print("\t| 0    0 |")
        print("\t|        |")
        print("\t|_0____0_|")
    if (no == 5 ):
        print("\t _______")
        print("\t| 0   0 |")
        print("\t|   0   |")
        print("\t|_0___0_|")
    if (no == 6 ):
        print("\t _______")
        print("\t| 0   0 |")
        print("\t| 0   0 |")
        print("\t|_0___0_|")
    print("\nPress (y) ==> ROLL","\nPress (x) ==> EXIT")
    temp = input()
    if ( temp == "x" ):
        break
