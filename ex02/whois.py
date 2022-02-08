import sys

l = len(sys.argv)
if l != 1:
    if l != 2:
        print("ERROR")
    else:
        try:
            number = int(sys.argv[1])
            if number == 0:
                print("I'm Zero.")
            elif number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except:
            print("ERROR")