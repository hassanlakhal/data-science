import sys
import string


def analyse_text(text: str):
    count_upper = count_lower = count_spaces = count_digit = count_marks = 0
    count = len(text)
    for char in text:
        if char.isupper():
            count_upper = count_upper + 1
        elif char.islower():
            count_lower = count_lower + 1
        elif char.isspace():
            count_spaces = count_spaces + 1
        elif char.isdigit():
            count_digit = count_digit + 1
        elif char in string.punctuation:
            count_marks = count_marks + 1
    print(
        f"The text contains {count} characters:\n"
        f"{count_upper} upper letters\n"
        f"{count_lower} lower letters\n"
        f"{count_marks} punctuation marks\n"
        f"{count_spaces} spaces\n"
        f"{count_digit} digits")


def main():
    len_args = len(sys.argv) - 1
    if len_args == 1:
        text = sys.argv[1]
        analyse_text(text)
    elif len_args == 0:
        print("What is the text to count?")
        text = sys.stdin.readline()
        analyse_text(text)
    else:
        raise AssertionError("Too many arguments")


if __name__ == "__main__":
    main()
