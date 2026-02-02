import sys

number_of_args = len(sys.argv) - 1

if number_of_args == 0:
    sys.exit()
elif number_of_args == 1:
    try:
        digit = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit()
    if digit % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")
else:
    print("AssertionError: more than one argument is provided")
