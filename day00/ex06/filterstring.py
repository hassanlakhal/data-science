import sys
from ft_filter import ft_filter

def main():
    len_args = len(sys.argv) - 1
    if len_args == 2:
        text = sys.argv[1]
        list_words = text.split()
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("AssertionError: the arguments are bad")
        new_list = ft_filter(lambda x: len(x) > number, list_words)
        print(f"{new_list}")
    
        

if __name__ == "__main__":
    main()