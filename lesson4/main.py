import utils.math_operations 
from utils.string_operations import to_uppercase, reverse_string

def main():
    # Math operations
    print("Addition:", utils.math_operations.add(5, 3))
    print("Subtraction:", utils.math_operations.subtract(10, 4))
    print("Multiplication:", utils.math_operations.multiply(2, 3))

    # String operations
    print("Uppercase:", to_uppercase("hello"))
    print("Reversed:", reverse_string("world"))

if __name__ == "__main__":
    main()