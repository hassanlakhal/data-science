import sys


def main():
    len_args = len(sys.argv) - 1
    if len_args == 2:
        text = sys.argv[1]
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("Argement number tow not a integer")
        

if __name__ == "__main__":
    main()