import sys


def main():
    NESTED_MORSE = {" ": "/",
                    "A": ".-",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-.",
                    "G": "--.",
                    "H": "....",
                    "I": "..",
                    "J": ".---",
                    "K": "-.-",
                    "L": ".-..",
                    "M": "--",
                    "N": "-.",
                    "O": "---",
                    "P": ".--.",
                    "Q": "--.-",
                    "R": ".-.",
                    "S": "...",
                    "T": "-",
                    "U": "..-",
                    "V": "...-",
                    "W": ".--",
                    "X": "-..-",
                    "Y": "-.--",
                    "Z": "--..",
                    "0": "-----",
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    }
    len_args = len(sys.argv) - 1
    if len_args == 1:
        text = sys.argv[1]
        text = text.upper()
        filter_text = [
            char for char in text
            if not char.isalnum() and not char.isspace()]
        if len(filter_text):
            print("AssertionError: the arguments are bad")
            sys.exit()
        for i, char in enumerate(text):
            if char in NESTED_MORSE:
                if i != len(text) - 1:
                    print(NESTED_MORSE[char], end=' ')
                else:
                    print(NESTED_MORSE[char])


if __name__ == "__main__":
    main()
