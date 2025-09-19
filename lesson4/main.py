from utils.math_operations import add, subtract
from utils.string_operations import to_uppercase, reverse_string

def main():
    # Math operations
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))

    # String operations
    print("Uppercase:", to_uppercase("hello"))
    print("Reversed:", reverse_string("world"))

if __name__ == "__main__":
    main()